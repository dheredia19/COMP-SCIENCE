a = []

print("Power Problems! Enter two numbers that represent your exponential.")
base = input("What is the base of your exponential? ")
power = input("What is the maximum exponent of your base? ")

try:
	base = int(base)
	power = int(base)
except:
	print("You fool! You did something wrong. Just type numerical numbers, it's simple!")
	quit()

for x in range(0,power+1):
	a.append(base ** x)
print(a)