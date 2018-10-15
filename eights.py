print("Because you are an illiterate moron, I will count the eights for you!")

getting = input("What do you want to count? ")

eights = 0

for x in range(len(getting)):
	if getting[x] == "8":
		eights += 1

print("You had " + str(eights) + " eights in your numeral. Go back to school!")