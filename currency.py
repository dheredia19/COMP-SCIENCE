print("Welcome to the currency calculatorinator.")
source = input("Please enter the currency to convert from: ")

if "dollar" in source:
	factor = 1
elif "euro" in source:
	factor = 0.86
elif "yen" in source:
	factor = 111.35
else:
	print("Your desired argument was not found.")
	quit()

source = input("Please enter the currency to convert to: ")

if "dollar" in source:
	factor = 1
elif "euro" in source:
	factor = 0.86
elif "yen" in source:
	factor = 111.35
else:
	print("Your desired argument was not found.")
	quit()