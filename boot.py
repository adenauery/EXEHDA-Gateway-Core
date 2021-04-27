from clock import Clock
from utils import log, start_time
from wifi import WiFi
from ota import OTA
from os import listdir
from machine import reset

try:
	WiFi()
	Clock()
	OTA()

	if 'main' in listdir():
		from main.init import start
		try:
			start()
		except Exception as e:
			log("APP: {}".format(e))
			reset()
	else:
		log("BOOT: main application not found")

except Exception as e:
	log("BOOT: {}".format(e))
	reset()
