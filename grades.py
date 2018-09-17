import sys

print("This is the Lean Mean Horrible Grading Machine.")

print("Detected Arguments:")
print("Number Grade: " + sys.argv[1])

try:
	grade = float(sys.argv[1])
except ValueError:
	print("What do you think this is? Type a number with a decimal! You fail!")
	quit()

if grade > 5.0:
	print("What do you think this is? A calculator? Type a number between 0 through 5! You fail!")
elif grade >= 4.85:
	print("You got an A+!")
	print("Perfect!")
elif grade >= 4.7:
	print("You got an A!")
	print("Stellar!")
elif grade >= 4.5:
	print("You got an A-!")
	print("Cool!")
elif grade >= 4.2:
	print("You got an B+!")
	print("Okay!")
elif grade >= 3.85:
	print("You got an B!")
	print("Average!")
elif grade >= 3.5:
	print("You got an B-!")
	print("Subpar!")
elif grade >= 3.2:
	print("You got an C+!")
	print("Unfortunate!")
elif grade >= 2.85:
	print("You got an C!")
	print("Poor!")
elif grade >= 2.5:
	print("You got an C-!")
	print("Sad!")
elif grade >= 2:
	print("You got an D+!")
	print("Bad!")
elif grade >= 1.5:
	print("You got an D!")
	print("Terrible!")
elif grade >= 1.0:
	print("You got an D-!")
	print("Abysmal!")
elif grade >= 0:
	print("You got an F!")
	print("You failed!")
else:
	print("What do you think this is? A calculator? Type a number between 0 through 5! You fail!")