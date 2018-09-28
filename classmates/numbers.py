import sys

a = []

print("I like numbers, so I expect a lot of them. You catch my drift?")

if len(sys.argv) < 11:
	count = str(len(sys.argv)-1)
	print("Clearly you did not understand my obsession with numbers. I want at least 10 of them, but you only gave me " + count + "!")
	quit()
elif len(sys.argv) > 11:
	count = str(len(sys.argv)-1)
	print("Hold your horses, cow-human. I'm not in the business of doing your math homework, as you gave me " + count + " numbers!")
	quit()

print("Detected arguments:")

for x in range(1,len(sys.argv)):
	count = str(x)
	print("Number " + count + " :", end = ' ')
	print(sys.argv[x])
	try:
		a.append(int(sys.argv[x]))
	except:
		say = str(sys.argv[x])
		print('Do you seriously expect me to believe that "' + say + '" is a number? I\'m not an idiot, you know.')
		quit()

print("Thank you for these numbers! Let's start by putting them into a nice list:")
print(a)
print("You know what would be cool? If we could make sure these were in order:")
a.sort()
print(a)
print("But that's for normies. Let's do something rebellious: flip the order!")
a.sort(reverse=True)
print(a)
print("Like I said, I love numbers. Why don't we add them up to get a bigger one?")
added = sum(a)
print(str(a[0]) + " + " + str(a[1]) + " + " + str(a[2]) + " + " + str(a[3]) + " + " + str(a[4]) + " + " + str(a[5]) + " + " + str(a[6]) + " + " + str(a[7]) + " + " + str(a[8]) + " + " + str(a[9]) + " = " + str(added))