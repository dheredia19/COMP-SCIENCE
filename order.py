import sys
import time

print("Hi. If you're trying to figure out if your numbers are in order, you've come to the right place.")
time.sleep(2)

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

a = int(x)
b = int(y)
c = int(z)

print("First, let's look at what you've brought to the table, shall we?")
print("First number: " + x)
print("Second number: " + y)
print("Third number: " + z)
time.sleep(3)

print("Well, the logical thing to do would be to test the first two numbers to see which way they are going.")
if a < b:
	print("It looks like your first number, " + x + ", is smaller than your second number, " + y + ".")
	time.sleep(3)
	print("Now, let's see how your first two numbers stack up against the third.")
	if c > b:
		print("Fantastic! Your third number, " + z + ", is greater than your second number, " + y + "!")
		print("This means that your numbers are in ascending order from " + x + "<" + y + "<" + z + ".")
	else:
		print("What's this? Your third number, " + z + ", is not in line with the others!")
		print("Come back when you have your numbers together, and not a minute sooner!")
else:
	print("It looks like your first number, " + x + ", is greater than your second number, " + y + ".")
	time.sleep(3)
	print("Now, let's see how your first two numbers stack up against the third.")
	if c < b:
		print("Fantastic! Your third number, " + z + ", is less than your second number, " + y + "!")
		print("This means that your numbers are in descending order from " + x + ">" + y + ">" + z + ".")
	else:
		print("What's this? Your third number, " + z + ", is not in line with the others!")
		print("Come back when you have your numbers together, and not a minute sooner!")