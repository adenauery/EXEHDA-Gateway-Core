from ntptime import settime
from _thread import start_new_thread
from time import sleep, localtime

from utils import log, start_time


class Clock:
	def __init__(self):
		self.set_clock()
		start_time()
		start_new_thread(self.refresh, ())

	def refresh(self):
		sleep(60 * 60 * 24)
		self.set_clock()

	def set_clock(self):
		try:
			settime()
		except Exception as e:
			log("CLOCK: {}".format(e))
		
		if int(localtime()[0]) > 2018:
			return True
		sleep(10)
		return self.set_clock()
