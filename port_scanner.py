#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
	print("Invalid amount of arguments!!!.")
	print("Syntax: pythoon3 port_scanner.py <ip> ")

#Add a Banner
print("-" * 50)
print("Scanning target " +target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(20,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\n Existing Program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")

	sys.exit()
except socket.error:
	print("Could not connect to server")
	sys.exit()