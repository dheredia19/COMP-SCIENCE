import random

print("This is a simple Minesweeper game, which you are destined to lose.")
height = input("How many rows do you want? ")
width = input("How many column do you want? ")

w = int(width)
h = int(height)

matrix = [[0]*w for i in range(h)]

def display():
	global x
	global y
	global matrix
	for x in range(h):
		for y in range(w):
			print(matrix[x][y], end = ' ')
		print()

display()

maxbombs = w*h
bombs = input("How many bombs do you want? ")
b = int(bombs)

if b > maxbombs:
	print("Yikes! You must be a terrorist, because that's more bombs than your grid can support!")
	quit()

result = None

def bomber():
	global result
	findX = random.randint(0,h)
	findY = random.randint(0,w)
	print("(" + str(findX) + "," + str(findY) + ")")
	matrix[findX][findY] = "*"

while result is None:
	try:
		for x in range(b):
			bomber()
		result = True
	except:
		matrix = [[0]*w for i in range(h)]

display()

for x in range(h):
	for y in range(w):
		if matrix[x][y] == "*":
			try:
				matrix[x-1][y-1] += 1
			except:
				pass
			try:
				matrix[x-1][y] += 1
			except:
				pass
			try:
				matrix[x-1][y+1] += 1
			except:
				pass
			try:
				matrix[x][y-1] += 1
			except:
				pass
			try:
				matrix[x][y+1] += 1
			except:
				pass
			try:
				matrix[x+1][y-1] += 1
			except:
				pass
			try:
				matrix[x+1][y] += 1
			except:
				pass
			try:
				matrix[x+1][y+1] += 1
			except:
				pass

print()
display()