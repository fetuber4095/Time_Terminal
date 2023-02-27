from os import system
from time import sleep
from random import randint
from getpass import getpass

__version__ = ["alpha b1.0.0", "Kernel Implement"]

class index:
	def __init__(self, user):
		print("Comming Soon. . .")
		input()

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
	index(x)

else:
	x = open("settings.json", "rt").read()
	x = x.slipt()
	while True:
		x2 = getpass(f"{x[0]}, password: ")
		if x2 = x[1]:
			index(x[0])
			break
		else:
			print("The password is incorrect!")
			