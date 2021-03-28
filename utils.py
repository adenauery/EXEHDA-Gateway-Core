from json import loads, dumps
from time import localtime


def get_configs():
	file = open('configs.json', 'r')
	configs = loads(file.read())
	file.close()
	return configs


def get_date():
	local_date = localtime()
	return "{}-{}-{}T{}:{}:{}.{}Z".format(local_date[0], local_date[1], local_date[2], local_date[3], local_date[4], local_date[5], local_date[6])


def log(data):
	log_data = "{}\n".format(dumps({"gathered_at": get_date(), "type": "log", "data": data}))
	print(log_data)
	
	file = open('log.txt', 'a')
	file.write(log_data)
	file.close()


def start_time():
	file = open('start_time.dat', 'w')
	file.write(get_date())
	file.close()
