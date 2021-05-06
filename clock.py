from machine import Pin, I2C, RTC
from ds3231_port import DS3231
from _thread import start_new_thread
from ntptime import settime
from time import sleep, localtime, time
from utils import log, start_time

I2C_RTC_SCL_PIN = Pin(22)
I2C_RTC_SDA_PIN = Pin(21)

class Clock:
	def __init__(self):
		try:
			i2c = I2C(scl = I2C_RTC_SCL_PIN, sda = I2C_RTC_SDA_PIN)
			self.rtc = DS3231(i2c)
		except:
			self.rtc = None

		self.set_clock()
		start_time()
		start_new_thread(self.refresh, ())

	def refresh(self):
		sleep(60 * 60 * 24)
		self.set_clock()

	def is_valid_time(self, time):
		return int(time[0]) > 2018
	
	def get_NTP(self, attempts):
		while attempts:
			attempts -= 1
			try:
				settime() # Set localtime from NTP
				if self.is_valid_time(localtime()):
					return True
			except:
				sleep(5)
		
		return False

	def set_clock(self):
		while(True):
			fail_notified = False
			attempts = 3
			if self.get_NTP(attempts):
				if self.rtc:
					self.rtc.save_time() # Set RTC from NTP  
				return True
			elif self.rtc: 
				rtc_time = self.rtc.get_time()
				if self.is_valid_time(rtc_time):
					# Set localtime from RTC
					tm = rtc_time
					RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
					return True
				elif not fail_notified:
						log("CLOCK: invalid time from RTC")
						fail_notified = True
			elif not fail_notified:
				log("CLOCK: RTC not found")
				fail_notified = True
			
			sleep(10)