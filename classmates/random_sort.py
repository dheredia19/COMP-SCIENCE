import random

a = []

print("You see, I could pick random numbers all day. But that wouldn't be fair to you.")
print("Thus, today I am seeking your input on this matter.")
print("These are my numbers:")

for x in range(1,16):
	count = str(x)
	number = random.randint(0,100)
	a.append(number)
	print("Number " + count + ":", end = ' ')
	print(number)

print("In list form, this would be:")
print(a)
user = input("Alrighty. Now that we've gotten that out of the way, what do you want your number to be? ")
try:
	get = int(user)
	a.append(get)
except:
	error = str(user)
	print('Good grief. "' + error + '"? ' + "Seriously? You had one job! ONE! I'm never asking you anything ever again!")
	quit()

print("Thanks! Let me sort the list with your number in it!")
a.sort(reverse = True)
print(a)