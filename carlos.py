'''
Google Maps Beta 0.39.44
What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time?
In our testing, the number at which the distance travelled would be 4 steps or less varied between trials.
Occasionally, a step count would give us over 50% walking distance results, where another would be over 50% public transit.
This issue could perhaps be resolved with more trials; however, the number of steps within walking distance became greater with more trials!

Monte Carlo Simulations Build 42069
What are they?
They are computational algorithims that solve problems using data from random sets to find a more probable answer.

What can they be used for?
They can be used to find values that would otherwise be difficult to exactly calculate, where using randomly generated values in function can more efficiently determine the answer.

How do they work?
In a function that can take a wide domain of values, a random number generator can be inputted to get a large data set of solutions.
The resulting data can then be compared with the expected or predicted value to determine whether the probability of the randomized solutions matches.
The simulation can be ran continuously to increase accuracy of the desired result.

'''

import random

tries = 1000000
bullseye = 0

for i in range(tries):
	x = random.random()*2-1
	y = random.random()*2-1
	#print(x,y)
	dist = x**2 + y**2
	#print(dist)
	if dist < 1:
		bullseye += 1
print(bullseye)

'''
What happened?
As we increased the number of iterations, the resulting percentage out of darts that hit the circle became more precise!
If we were to graph the circle and the location of the darts, the more times the simulation is ran, we can better see what the spread of darts across the dartboard is over time.
This would in theory allow someone to calculate the size of the circle if we do not have the information that we used to generate it in the simulation.

'''
