from ntptime import settime
from _thread import start_new_thread
from time import sleep, localtime, time

from utils import log, start_time


class Clock:
	def __init__(self):
		self.set_clock()
		start_time()
		start_new_thread(self.refresh, ())

	def refresh(self):
		sleep(60 * 60 * 24)
		self.set_clock()
	
	def get_posix_timestamp(self):
		# time() return timestamp from 2000-01-01 00:00:00 UTC
		# while the posix timestamp 1970-01-01 00:00:00 UTC 
		return time() + 946684800
		
	def set_clock(self):
		try:
			settime()
		except Exception as e:
			log("CLOCK: {}".format(e))
		
		if int(localtime()[0]) > 2018:
			return True
		sleep(10)
		return self.set_clock()
