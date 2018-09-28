import sys

a = []

print("Given what you've entered, we're going to collect and get rid of the basket of deplorables.")

print("Detected arguments:")
for x in range(1,len(sys.argv)):
	count = str(x)
	print("String " + count + ":", end = ' ')
	print(sys.argv[x])
	a.append(sys.argv[x])

print("Great, now we got our strings. If you want proof, this is their representation as a list:")
print(a)
print("Next, we're going to go through each one to check if it belongs in the basket of deplorables.")
print('These are strings that contain the letter "a".')

for x in range(0,len(a)):
	print("Let's see if " + a[x] + " is a deplorable.")
	if "a" in a[x]:
		print("Aha! It's a bad apple! It shall be removed from the list at once!")
		a.pop(x)
	else:
		print("Nope, this one is good to go.")

print("Alrighty! Let's see what we got!")
print(a)