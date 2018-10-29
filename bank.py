from os import system, name
import random
import re
import sys

accounts = []

class account:
	def __init__(self, number, name, pin, ssn):
		self.number = number
		self.name = name
		self.balance = 50.00
		self.pin = pin
		self.ssn = ssn

def clear(): 
	# for windows 
	if name == 'nt':
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')
	header()

def pause():
	input("Press ENTER to continue...")

def header():
	print("________________")
	print("BANK TELLER 3000")
	print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def start():
	clear()
	print("Please sign in to your Account. To create a new account, leave the field blank.")
	signon = input()

	if signon == "":
		sign_up()
	try:
		for i in accounts:
			if int(signon) == i.number:
				print("Hello, " + i.name + "! Please enter your PIN.")
				test_pin = input()
				if test_pin != i.pin:
					print("The PIN you have provided is not correct. Please try again.")
					pause()
					start()
				menu(i)
			else:
				print("The account number you provided was not found. Please try again.")
				pause()
				start()
	except ValueError:
		print("The account number you provided was invalid. Please try again.")
		pause()
		start()

def sign_up():
	print("Welcome to our bank network. Please enter your name:")
	new_name = input()
	if new_name is "":
		print("Your name was left blank. Please try again.")
		pause()
		start()
	print("Hello, " + new_name + ". Please create a four to eight digit PIN:")
	new_pin = input()
	if 4 <= len(new_pin) <= 8:
		pass
	else:
		print("Your PIN was not valid. Please try again.")
		pause()
		start()
	print("For security, please enter your Social Security Number:")
	s = input()
	r = re.compile('.{3}-.{2}-.{4}')
	if len(s) == 11:
		if r.match(s):
			print("Your details have been saved successfully.")
			new_ssn = s
		else:
			print("Your Social Security Number is not valid. Please try again.")
			pause()
			start()
	else:
		print("Your Social Security Number is not valid. Please try again.")
		pause()
		start()

	new_account = random.randint(10000000,99999999)
	# Method from (http://introtopython.org/classes.html#Making-multiple-objects-from-a-class) [IntroToPython]
	temp_account = account(new_account, new_name, new_pin, new_ssn)
	accounts.append(temp_account)
	print("Thank you for banking with us! Your account number is " + str(new_account) + ".")
	print("As a complimentary gift for opening your account, we would like to give you an initial deposit of $50.00. Enjoy!")
	pause()
	start()

def menu(loggedin):
	clear()
	print("---Main Menu---")
	print("Please select an option. You can:")
	print("   1. Make a withdrawal")
	print("   2. Make a deposit")
	print("   3. View/change your information")
	print("   4. End your banking session")
	try:
		choice = int(input())
		if choice == 1:
			print("How much would you like to withdraw?")
			dollar = input()
			try:
				dollar = int(dollar)
				print("Success!")
				pause()
				menu(loggedin)
			except ValueError:
				print("The amount you entered is invalid. Please try again.")
				pause()
				menu(loggedin)
		elif choice == 2:
			print("How much would you like to deposit?")
			dollar = input()
			try:
				dollar = int(dollar)
				print("Success!")
				pause()
				menu(loggedin)
			except ValueError:
				print("The amount you entered is invalid. Please try again.")
				pause()
				menu(loggedin)
		elif choice == 3:
			print("---Current Account Info---")
			print("Account Number: " + str(loggedin.number))
			print("Account Holder: " + str(loggedin.name))
			print("Balance: " + str(loggedin.balance))
			print("PIN: " + str(loggedin.pin))
			print("Social Security Number: " + str(loggedin.ssn))
			pause()
			menu(loggedin)
		elif choice == 4:
			print("Are you sure you want to quit?")
			if "y" in input():
				end()
			else:
				menu(loggedin)
		else:
			print("The selection you made is invalid. Please try again.")
			pause()
			menu(loggedin)
		menu(loggedin)
	except ValueError:
		print("The selection you made is invalid. Please try again.")
		pause()
		menu(loggedin)

def end():
	print("You have been logged out of your banking session.")
	pause()
	quit()

try:
	start()
except KeyboardInterrupt:
	end()