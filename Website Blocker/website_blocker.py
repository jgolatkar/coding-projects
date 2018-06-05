#!/usr/bin/env python

import sys
import time
from datetime import datetime as dt

hosts_path = '/etc/hosts'
redirect = '127.0.0.1'

black_list = ['www.facebook.com','facebook.com','www.reddit.com']

while True:
	if 8 < dt.now().hour < 16:
		with open(hosts_path,'r+') as file:
			content = file.read()
			for website in black_list:
				if website not in content:
					file.write(redirect+'   '+website+'\n')
		time.sleep(5)
	else:
		with open(hosts_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in black_list):
					file.write(line)
			file.truncate()
		sys.exit()
