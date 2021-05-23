from machine import Timer, reset
from utils import log

class Watchdog :
	def __init__(self, timeout):
		self.timer = Timer(2)
		self.timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:self.wdt())
		self.timeout = timeout
		self.cnt = timeout

	def wdt(self):
		self.cnt -= 1
		if self.cnt <= 0:
			log("WDT: timeout")
			reset()
	
	def feed(self):
		self.cnt = self.timeout
