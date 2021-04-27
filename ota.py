import socket
import os
import gc
import json
import ssl

from utils import log, get_configs


class OTA:
	def __init__(self):
		configs = get_configs()

		self.token = configs['git']['token']
		self.url = configs['git']['url']
		self.uuid = configs['gateway']['uuid']

		self.http_client = HttpClient(headers={'Authorization': 'token {}'.format(self.token)})
		self.github_repo = self.url.rstrip('/').replace('https://github.com', 'https://api.github.com/repos')
		self.main_dir = "main"
		self.module = ''

		self.download_updates_if_available()
		self.apply_pending_updates_if_available()

	def apply_pending_updates_if_available(self):
		try:
			if 'next' in os.listdir(self.module):
				if '.version' in os.listdir(self.module_path('next')):
					if self.module_path(self.main_dir) in os.listdir():
						self.rmtree(self.module_path(self.main_dir))
					os.rename(self.module_path('next'), self.module_path(self.main_dir))
					log("OTA: updated code")
				else:
					self.rmtree(self.module_path('next'))
		except Exception as e:
			log("OTA: {}".format(e))

	def download_updates_if_available(self):
		try:
			current_version = self.get_version(self.module_path(self.main_dir))
			latest_version = self.get_latest_version()

			if latest_version > current_version:
				if 'next' in os.listdir():
					self.rmtree('next')
				os.mkdir(self.module_path('next'))
				self.download_all_files(self.github_repo + '/contents/', latest_version)

				file = open(self.module_path('next/.version'), 'w')
				file.write(latest_version)
				file.close()

				log("OTA: successful download, version: " + latest_version)

		except Exception as e:
			log("OTA: {}".format(e))
			if 'next' in os.listdir():
				self.rmtree('next')

	def rmtree(self, directory):
		for entry in os.ilistdir(directory):
			if entry[1] == 0x4000:
				self.rmtree(directory + '/' + entry[0])
			else:
				os.remove(directory + '/' + entry[0])
		os.rmdir(directory)

	def get_version(self, directory, version_file_name='.version'):
		if directory in os.listdir():
			if version_file_name in os.listdir(directory):
				file = open(directory + '/' + version_file_name)
				version = file.read()
				file.close()
				return version
		return '0.0'

	def get_latest_version(self):
		latest_release = self.http_client.get(self.github_repo + '/releases/latest')
		version = latest_release.json()['tag_name']
		latest_release.close()
		return version

	def download_all_files(self, root_url, version):
		file_list = self.http_client.get(root_url + '?ref=refs/tags/' + version)
		for file in file_list.json():
			if file['type'] == 'file':
				if file['path'] != '.gitignore' and file['path'] != 'README.md':
					download_url = file['download_url']
					download_path = self.module_path('next/' + file['path'])
					self.download_file(download_url.replace('refs/tags/', ''), download_path)
			elif file['type'] == 'dir':
				if file['name'] != 'tests':
					path = self.module_path('next/' + file['path'])
					os.mkdir(path)
					self.download_all_files(root_url + '/' + file['name'], version)
		file_list.close()

	def download_file(self, url, path):
		try:
			file = open(path, 'w')
			response = self.http_client.get(url)
			file.write(response.text)
		finally:
			response.close()
			file.close()
			gc.collect()

	def module_path(self, path):
		return self.module + '/' + path if self.module else path


class Response:
	def __init__(self, f):
		self.raw = f
		self.encoding = 'utf-8'
		self._cached = None

	def close(self):
		if self.raw:
			self.raw.close()
			self.raw = None
		self._cached = None

	@property
	def content(self):
		if self._cached is None:
			try:
				self._cached = self.raw.read()
			finally:
				self.raw.close()
				self.raw = None
		return self._cached

	@property
	def text(self):
		return str(self.content, self.encoding)

	def json(self):
		return json.loads(self.content)


class HttpClient:
	def __init__(self, headers={}):
		self._headers = headers

	def request(self, method, url, data=None, json=None, headers={}):
		def _write_headers(sock, _headers):
			for k in _headers:
				sock.write(b'{}: {}\r\n'.format(k, _headers[k]))

		try:
			proto, dummy, host, path = url.split('/', 3)
		except ValueError:
			proto, dummy, host = url.split('/', 2)
			path = ''
		if proto == 'http:':
			port = 80
		elif proto == 'https:':
			port = 443
		else:
			raise ValueError('Unsupported protocol: ' + proto)

		if ':' in host:
			host, port = host.split(':', 1)
			port = int(port)

		ai = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)
		ai = ai[0]

		s = socket.socket(ai[0], ai[1], ai[2])
		try:
			s.connect(ai[-1])
			if proto == 'https:':
				s = ssl.wrap_socket(s)
			s.write(b'%s /%s HTTP/1.0\r\n' % (method, path))
			if 'Host' not in headers:
				s.write(b'Host: %s\r\n' % host)
			_write_headers(s, self._headers)
			_write_headers(s, headers)

			s.write(b'User-Agent')
			s.write(b': ')
			s.write(b'MicroPython OTAUpdater')
			s.write(b'\r\n')
			if json is not None:
				assert data is None
				data = json.dumps(json)
				s.write(b'Content-Type: application/json\r\n')
			if data:
				s.write(b'Content-Length: %d\r\n' % len(data))
			s.write(b'\r\n')
			if data:
				s.write(data)

			l = s.readline()
			l = l.split(None, 2)
			status = int(l[1])
			reason = ''
			if len(l) > 2:
				reason = l[2].rstrip()
			while True:
				l = s.readline()
				if not l or l == b'\r\n':
					break
				if l.startswith(b'Transfer-Encoding:'):
					if b'chunked' in l:
						raise ValueError('Unsupported ' + l)
				elif l.startswith(b'Location:') and not 200 <= status <= 299:
					raise NotImplementedError('Redirects not yet supported')
		except OSError:
			s.close()
			raise

		resp = Response(s)
		resp.status_code = status
		resp.reason = reason
		return resp

	def head(self, url, **kw):
		return self.request('HEAD', url, **kw)

	def get(self, url, **kw):
		return self.request('GET', url, **kw)

	def post(self, url, **kw):
		return self.request('POST', url, **kw)

	def put(self, url, **kw):
		return self.request('PUT', url, **kw)

	def patch(self, url, **kw):
		return self.request('PATCH', url, **kw)

	def delete(self, url, **kw):
		return self.request('DELETE', url, **kw)
