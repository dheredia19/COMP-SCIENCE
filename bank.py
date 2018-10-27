class account:
	def __init__(self):
		self.user = ""
		self.name = ""
		self.balance = 0.00
		self.pin = 0
		self.ssn = ""

from os import system, name
def clear(): 
	# for windows 
	if name == 'nt':
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

def header():
	print("________________")
	print("BANK TELLER 3000")
	print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def start():
	print("Please sign in to your Account. To create a new account, leave the field blank.")
	signon = input()

	if signon == "":
		new_account()
	if signon in account.user:
		print("Hello, " + )

def new_account():
	print("Welcome to our bank network. Please enter your name:")
	new_name = input()
	print("Please create a four to eight digit pin:")
	new_pin = input()
	print("Please enter your Social Security Number:")
	new_ssn = input()
	print("As a complimentary ")