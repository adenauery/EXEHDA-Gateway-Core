from clock import Clock
from utils import log, start_time
from wifi import WiFi
from ota import OTA
from os import listdir
from machine import reset

try:
	start_time()
	WiFi()
	Clock()
	OTA()

	if 'main' in listdir():
				from main.init import start
				start()
	else:
		log("falta pasta main")

except Exception as e:
	log("boot.py: {}".format(e))
	reset()
