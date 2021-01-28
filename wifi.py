import pages

from time import sleep
from _thread import start_new_thread
from re import search

import socket
import network

from utils import get_configs

NETWORK_PROFILES = 'wifi.dat'


class WiFi:
	def __init__(self):
		configs = get_configs()

		self.project_name = configs['project_name']
		self.ap_ssid = self.project_name
		self.ap_password = ""
		self.ap_authmode = 0
		self.wlan_ap = network.WLAN(network.AP_IF)
		self.wlan_sta = network.WLAN(network.STA_IF)
		self.server_socket = None

		self.get_connection()

	def read_profiles(self):
		profiles = {}
		try:
			with open(NETWORK_PROFILES) as f:
				lines = f.readlines()

			for line in lines:
				ssid, password = line.strip("\n").split(";")
				profiles[ssid] = password
		except OSError:
			pass
		return profiles

	def write_profiles(self, profiles):
		lines = []
		for ssid, password in profiles.items():
			lines.append("{};{}\n".format(ssid, password))
		with open(NETWORK_PROFILES, "w") as f:
			f.write(''.join(lines))

	def do_connect(self, ssid, password):
		self.wlan_sta.active(True)
		if self.wlan_sta.isconnected():
			return None

		self.wlan_sta.connect(ssid, password)
		connected = None
		for _ in range(100):
			connected = self.wlan_sta.isconnected()
			if connected:
				break
			sleep(0.1)
		if not connected:
			self.wlan_sta.disconnect()
		return connected

	def send_header(self, client, status_code=200):
		client.sendall("HTTP/1.0 {} OK\r\n".format(status_code))
		client.sendall("Content-Type: text/html\r\n")
		client.sendall("\r\n")

	def send_response(self, client, payload):
		client.sendall(payload)
		client.close()

	def decode(self, string):
		return string.replace("%20", " ").replace("%60", "`").replace("%27", "'").replace("%22", '"').replace("%3B", ";") \
			.replace("%3A", ":").replace("%7E", "~").replace("%3D", "=").replace("%2B", "+").replace("%2C", ",") \
			.replace("%3F", "?").replace("%7C", "|").replace("%2F", "/").replace("%5C", "\\").replace("%28", "(") \
			.replace("%29", ")").replace("%5B", "[").replace("%5D", "]").replace("%7B", "{").replace("%7D", "}") \
			.replace("%3C", "<").replace("%3E", ">").replace("%2E", ".").replace("%2D", "-").replace("%5F", "_") \
			.replace("%21", "!").replace("%40", "@").replace("%23", "#").replace("%24", "$").replace("%25", "%") \
			.replace("%5E", "^").replace("%26", "&").replace("%2A", "*")

	def handle_root(self, client):
		self.wlan_sta.active(True)

		self.send_header(client)

		networks = self.wlan_sta.scan()

		wifi_list = []
		count = 0
		for ssid, _, _, rssi, _, _ in sorted(networks, key=lambda x: x[3], reverse=True):
			ssid = ssid.decode('utf-8')
			wifi_list.append([ssid, rssi, str(count)])
			count += 1

		client.sendall(pages.main(self.project_name, wifi_list))
		client.close()

		return wifi_list

	def handle_configure(self, client, request, wifi_list):
		match = search("ssid=([^&]*)&password=(.*)", request)

		self.send_header(client)

		if match is None:
			self.send_response(client, pages.parameter_not_found(self.project_name))
			return False

		try:
			ssid = self.decode(match.group(1).decode("utf-8"))
			password = self.decode(match.group(2).decode("utf-8"))
		except Exception:
			ssid = self.decode(match.group(1))
			password = self.decode(match.group(2))

		if len(ssid) == 0:
			self.send_response(client, pages.ssid_not_found(self.project_name))
			return False

		for ssid_list, _, count in wifi_list:
			if ssid == count:
				ssid = ssid_list

		if self.do_connect(ssid, password):
			self.send_response(client, pages.success(self.project_name, ssid))

			profiles = {ssid: password}
			self.write_profiles(profiles)

			return True

		self.send_response(client, pages.failure(self.project_name, ssid))
		return False

	def close_server_socket(self):
		if self.server_socket:
			self.server_socket.close()
			self.server_socket = None

	def access_point(self):
		if self.read_profiles():
			sleep(15)

			if self.wlan_sta.isconnected():
				return

		addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

		self.close_server_socket()

		self.wlan_sta.active(True)
		self.wlan_ap.active(True)

		self.wlan_ap.config(essid=self.ap_ssid, password=self.ap_password, authmode=self.ap_authmode)

		self.server_socket = socket.socket()
		self.server_socket.bind(addr)
		self.server_socket.listen(1)

		wifi_list = []

		while True:
			if self.wlan_sta.isconnected():
				break

			try:
				client, addr = self.server_socket.accept()
			except OSError:
				break

			try:
				client.settimeout(1.0)

				request = b""
				try:
					while "\r\n\r\n" not in request:
						request += client.recv(512)
				except OSError:
					pass

				try:
					request += client.recv(512)
				except OSError:
					pass

				try:
					url = search("(?:GET|POST) /(.*?)(?:\\?.*?)? HTTP", request).group(1).decode("utf-8").rstrip("/")
				except Exception:
					url = search("(?:GET|POST) /(.*?)(?:\\?.*?)? HTTP", request).group(1).rstrip("/")

				try:
					if url == "":
						wifi_list = self.handle_root(client)
					elif url == "configure":
						self.handle_configure(client, request, wifi_list)
					else:
						self.send_response(client, pages.not_found(self.project_name))
				except OSError:
					pass
			finally:
				client.close()

	def try_connect(self):
		while True:
			if self.wlan_sta.isconnected():
				return self.wlan_sta

			profiles = self.read_profiles()

			if profiles:
				self.wlan_sta.active(True)
				networks = self.wlan_sta.scan()

				for ssid, _, _, _, authmode, _ in sorted(networks, key=lambda x: x[3], reverse=True):
					ssid = ssid.decode('utf-8')
					connected = False

					if authmode > 0:
						if ssid in profiles:
							password = profiles[ssid]
							connected = self.do_connect(ssid, password)
					else:
						connected = self.do_connect(ssid, None)
					if connected:
						break
			sleep(10)

	def get_connection(self):
		if self.wlan_sta.isconnected():
			return True

		sleep(3)
		start_new_thread(self.access_point, ())
		connected = self.try_connect()

		self.close_server_socket()
		self.wlan_ap.active(False)

		sleep(2)
		return True if connected else None
