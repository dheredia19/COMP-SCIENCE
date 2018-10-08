import random

# Provision for subscript text (StackOverflow) [https://stackoverflow.com/questions/24391892/printing-subscript-in-python]
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

print("This is a simple Minesweeper game, which you are destined to lose.")
height = input("How many rows do you want? ")
width = input("How many columns do you want? ")
bombs = input("How many bombs do you want? ")

# Catch for non-number user inputs
try:
	# Set params for grid to exceed printed range
	w = int(width)+2
	h = int(height)+2
	b = int(bombs)
except ValueError:
	print("Can you try typing in regular numbers next time?")
	quit()

# Initialize game grids
solved = [[int("0")]*w for i in range(h)]
covered = [["■"]*w for i in range(h)]

# Print revealed game screen for computations
def showing():
	global x
	global y
	global solved
	print(" ", end = ' ')
	for y in range(1,w-1):
		print(str(y).translate(SUB), end = ' ')
	print()
	# Set params for grid to exceed printed range
	for x in range(1,h-1):
		print(str(x).translate(SUB), end = ' ')
		for y in range(1,w-1):
			print(solved[x][y], end = ' ')
		print()
	print()

# Print covered game screen for user
def hiding():
	global x
	global y
	global covered
	print(" ", end = ' ')
	for y in range(1,w-1):
		print(str(y).translate(SUB), end = ' ')
	print()
	# Set params for grid to exceed printed range
	for x in range(1,h-1):
		print(str(x).translate(SUB), end = ' ')
		for y in range(1,w-1):
			print(covered[x][y], end = ' ')
		print()
	print()

# Restrict number of spaces
if w < 10 or h < 10:
	print("What kind of Minesweeper do you play? This ain't supposed to be no walk in the park!")
	quit()

# Restrict number of bombs
maxbombs = w*h
if b > maxbombs:
	print("Yikes! You must be a terrorist, because that's more bombs than your grid can support!")
	quit()

# Reset game variables
result = None
correct = 0

def bomber():
	global result
	# Set params for grid to exceed printed range
	findX = random.randint(1,h-2)
	findY = random.randint(1,w-2)
	# print("(" + str(findX) + "," + str(findY) + ")")
	solved[findX][findY] = "*"

# Display initial hidden grid
print()
print("Let's start the game!")
hiding()

# Recalculate bomb grid until bomber function succeeds
while result is None:
	try:
		for x in range(b):
			bomber()
		result = True
	except:
		solved = [[0]*w for i in range(h)]

# First run of game loop to calculate bombs around selection
try:
	while True:
		row = input("Which row will you like to select? ")
		column = input("Which column will you like to select? ")
		# Catch for inputs that are not numbers
		try:
			r = int(row)
			c = int(column)
		except ValueError:
			# Prompt user for flag coordinates
			if "f" in str(row) or "f" in str(column):
				row = input("Which row should the flag go? ")
				column = input("Which column should the flag go? ")
				# Catch for inputs that are not numbers
				try:
					r = int(row)
					c = int(column)
					# Catch for numbers that are too big
					try:
						covered[r][c] = "►"
						hiding()
					except IndexError:
						print("C'mon! Your inputs are out of the range!")
						continue
				except ValueError:
					print("Can you try typing in regular numbers, then?")
					continue
			print("Can you try typing in regular numbers, then?")
			continue
		# Catch for numbers that are too big
		try:
			covered[r][c] = str(solved[r][c])
			if "0" in covered[r][c]:
				for i in range(-1, 2):
					if "0" in covered[r+1][c+i]:
						print("(" + str(r+1) + "," + str(c+i) + ") is clear!")
					else:
						print("(" + str(r+1) + "," + str(c+i) + ") is not clear!")
		except IndexError:
			print("C'mon! Your inputs are out of the range!")
			continue
		hiding()
		break
except KeyboardInterrupt:
	print()
	print("Ha! You fool! I knew you would chicken out. Now get lost!")
	quit()

# Calculate bomb counts in surrounding spaces
for x in range(h):
	for y in range(w):
		if solved[x][y] == "*":
			try:
				solved[x-1][y-1] += 1
			except:
				pass
			try:
				solved[x-1][y] += 1
			except:
				pass
			try:
				solved[x-1][y+1] += 1
			except:
				pass
			try:
				solved[x][y-1] += 1
			except:
				pass
			try:
				solved[x][y+1] += 1
			except:
				pass
			try:
				solved[x+1][y-1] += 1
			except:
				pass
			try:
				solved[x+1][y] += 1
			except:
				pass
			try:
				solved[x+1][y+1] += 1
			except:
				pass

# Game loop to catch Ctrl-C
try:
	while True:
		row = input("Which row will you like to select? ")
		column = input("Which column will you like to select? ")
		# Catch for inputs that are not numbers
		try:
			r = int(row)
			c = int(column)
		except ValueError:
			# Prompt user for flag coordinates
			if "f" in str(row) or "f" in str(column):
				row = input("Which row will you like to select? ")
				column = input("Which column will you like to select? ")
				# Catch for inputs that are not numbers
				try:
					r = int(row)
					c = int(column)
					# Catch for numbers that are too big
					try:
						covered[r][c] = "►"
						# Check if correct flag placement
						if "*" in str(solved[r][c]):
							correct += 1
						else:
							correct -= 1
						# Win sequence
						if correct == b:
							print("Wow! You actually won the game! Now get lost!")
							quit()
						hiding()
					except IndexError:
						print("C'mon! Your inputs are out of the range!")
						continue
				except ValueError:
					print("Can you try typing in regular numbers, then?")
					continue
			else:
				print("Can you try typing in regular numbers, then?")
			continue
		# Catch for numbers that are too big
		try:
			covered[r][c] = str(solved[r][c])
		except IndexError:
			print("C'mon! Your inputs are out of the range!")
			continue
		# Jump out of loop if bomb uncovered
		if "*" in covered[r][c]:
			print("Ha! You fool! You landed on a bomb. Now get lost!")
			showing()
			quit()
		else:
			hiding()
except KeyboardInterrupt:
	print()
	print("Ha! You fool! I knew you would chicken out. Now get lost!")