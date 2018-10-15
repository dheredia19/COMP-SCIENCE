print("I will count up the amount of decades in your Roman Numberal. Et tu, Servius?")

roman = input("What do you want to count? ")

loops = 0
xs = 0

def count(xs, loops):
	if roman[xs] == "x":
		print("yay")
		xs += 1
	loops += 0
	count(xs, loops)

count(xs, loops)

"""
for x in range(len(roman)):
	if roman[x] == "x":
		xs += 1
"""

print("You had " + str(xs) + " decades in your numeral. Get with the program, old-timer!")