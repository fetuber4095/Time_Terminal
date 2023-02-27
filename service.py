from os import system, mkdir, chdir, startfile, rename, replace, listdir
from time import sleep
from random import randint
from getpass import getpass

import socket
import platform

__version__ = ["snapshot 12w08", "Terminal Bug Fix"]
__os__ = platform.system()



tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

def download(url):
	system(f"wget {url}")

def clear():
	if __os__ == 'linux':
		system("clear")
	else:
		system("cls")
	pass

class index:
	def __init__(self, user, pword):
		self.player = user
		self.password = pword
		self.appname = "Time Terminal"
		self.appdata = "settings.json"
		self.prompt = f"{self.player}@{IPAddr}:~$ "
		self.index()

	def index(self):
		clear()
		print(f"Welcome, {self.player} - {self.appname} [{__version__[0]} - {__version__[1]}]")
		while True:
			try:
				cmd = input(self.prompt).strip()
				if cmd.startswith("/"):
					cmd = self.getcmd(cmd, "/")
					if cmd == "exit":
						print("Goodbye. . .")
						input("")
						break
					elif cmd == "clear" or cmd == "cls":
						clear()
					elif cmd.startswith("echo"):
						cmd = self.getcmd(cmd, "echo")
						if cmd == "":
							print("")
						elif cmd.startswith("-c"):
							cmd = cmd.replace("-c ", "")
							cmd = cmd.replace("-c", "")
							self.prompt = cmd
						elif cmd == "-d":
							self.prompt = f"{self.player}@{hostname}:~$ " 
						else:
							print(cmd)
					elif cmd.startswith("lagg"):
						cmd = cmd.replace("lagg ", "")
						cmd = cmd.replace("lagg", "")
						if cmd == "install":
							print("To install use: 'install lagg'")
						elif cmd == "" or cmd == "start":
							try:
								startfile("lagg.exe")
							except FileNotFoundError:
								print("The LAGG plugin isnt installed")
								print("To install use: 'install lagg'")
					elif cmd.startswith("install"):
						cmd = self.getcmd(cmd, "install")
						try:
							if cmd == "lagg":
								print("To install LAGG you need to give permission to the Console")
								x = getpass(f"password for {self.player}: ")
								if x == self.password:
									if __os__ == 'linux':
										print("The LAGG Program just can be executed at Windows NT")
									else:
										input("fetching the source code of pkg https://download2282.mediafire.com/cj63qwx3422g/aek61ef2xbxhryd/ReduceMemory.exe:")
										system("wget https://download2282.mediafire.com/8qpnkwjwwdogJWRbwyied2oAcHy0Ai79y5dPGQHpvPiqtQ24H1fp_qlQFNylZ75cE9NX3aVCCwdXT0T03PNil36yTuztn6I/530b6jocges4x4i/ReduceMemory.exe")
										rename("ReduceMemory.exe", "lagg.exe")
										print("The LAGG Plugin was installed.")
								else:
									print(f"This isnt the password for {self.player}")
							elif cmd == "git":
								print("To install GIT you need to give permission to the Console")
								x = getpass(f"password for {self.player}: ")
								if x == self.password:
									if __os__ == 'linux':
										print("Comming Soon. . . ")
									else:
										input("fetching the source code of https://github.com/git-for-windows/git/releases/download/v2.39.0.windows.2/Git-2.39.0.2-32-bit.exe:")
										system("wget https://github.com/git-for-windows/git/releases/download/v2.39.0.windows.2/Git-2.39.0.2-32-bit.exe")
										rename("Git-2.39.0.2-32-bit.exe", "git-installer.exe")
										print("Opening the GIT Installer. . .")
										startfile("git-installer.exe")
								else:
									print(f"This isnt the password for {self.player}")
							

							else:
								print("This package doenst exists")		
						except FileNotFoundError:
							print("Sorry! Your connection with the internet is bad!")
							print("Installation failed.")
					else:
						cmd = cmd.split()
						print(f"{cmd[0]}: Unknow Command Error")
					print("")
				else:
					print(f"{self.player}@{IPAddr}: {cmd}\n")
			except KeyboardInterrupt:
					print("\nGoodbye. . .")
					input("")
					break

	def getcmd(self, cmd, ignore):
		x = cmd.replace(f"{ignore} ", "")
		x = x.replace(f"{ignore}", "")
		return x
	 	
try:
	x = open("settings.json")
	x.close()
except FileNotFoundError:
	clear()
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
	clear()
	x = open("settings.json", "rt").read()
	x = x.split()
	while True:
		x2 = getpass(f"{x[0]}, password: ")
		if x2 == x[1]:
			index(x[0], x[1])
			break
		else:
			print("The password is incorrect!")
			