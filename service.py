from os import system
from time import sleep
from random import randint
from getpass import getpass

import socket

__version__ = ["alpha c1.0.5", "Shell Implement"]


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

class index:
	def __init__(self, user):
		self.player = user
		self.appname = "Time Terminal"
		self.appdata = "settings.json"
		self.index()

	def index(self):
		print(f"Welcome, {self.player} - {self.appname} [{__version__[0]} - {__version__[1]}]")
		while True:
			try:
				cmd = input(f"{self.player}@{IPAddr}:~$ ").strip()
				if cmd == "exit":
					print("Goodbye. . .")
					input("")
					break



				else:
					cmd = cmd.split()
					print(f"{cmd[0]}: Unknow Command Error")
			except KeyboardInterrupt:
					print("\nGoodbye. . .")
					input("")
					break

					
try:
	x = open("settings.json")
	x.close()
except FileNotFoundError:
	print("Hello, Is good see you here!")
	print("Please register an user to you can acess the Terminal")
	x = input("username: ").strip()
	x2 = getpass(f"create an password for {x}: ").strip()
	x3 = open("settings.json", "wt+")
	x3.write(f"{x} {x2}")
	user = x
	password = x2
	del x, x2, x3
	index(user)

else:
	x = open("settings.json", "rt").read()
	x = x.split()
	while True:
		x2 = getpass(f"{x[0]}, password: ")
		if x2 == x[1]:
			index(x[0])
			break
		else:
			print("The password is incorrect!")
			