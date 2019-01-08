"""
Arbitrary Game Show Simulator 3000
Essentially, it would be advantageous for the contestant to switch the box that they are holding.
This conclusion results from the game show host removing one of the False options, which limits the choice to 2.
In this way, switching your box adjusts the probability of success from 1/3 to 1/2.
By not switching you are subject to the same 1/2 chance you began with.

"""

import random

outcome = []
winfirst = 0
winsecond = 0

def rand(skip):
	value = False
	while value in skip or r is False:
		value = random.randint(1,3)
	return value

for i in range(1000):
	car = random.randint(1,3)
	picked = random.randint(1,3)
	if car == picked:
		winfirst += 1
	else:
		pass
print("Wins: " + str(winfirst))

for i in range(1000):
	car = random.randint(1,3)
	first = random.randint(1,3)
	penny = rand([car,first])
	second = rand([first,penny])
	if car == second:
		winsecond += 1
	else:
		pass
print("Wins: " + str(winsecond))

"""
Based on the results, we can clearly see the difference of resulting values between the two cases.
In the second case, we gain a higher probability of success by removing one of the values from the choices.
This proves the original hypothesis that switching your box makes a considerable difference in success.

"""
