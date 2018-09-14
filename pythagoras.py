import math

x = 0.0

while x < 2*math.pi:
	print('Current angle in radians: ', end='')
	print(x)
	compute = (math.sin(x))**2 + (math.cos(x))**2
	print('Current output: ', end='')
	print(compute)
	x = x + 0.1