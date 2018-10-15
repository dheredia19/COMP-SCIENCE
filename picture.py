from PIL import Image
import os

print("We're going to make a checkerboard so I can kick your behind at chess.")
squares = input("In order to do that, you gotta tell me how many squares you want in the dimensions! ")

try:
	side = int(squares)
except:
	print("I need a number, you dummy! You'll never be good at chess at this rate...")
	quit()

dimension = side * 20
x = y = 0
alt = 20
number = range(0,side)
print(number)

board = Image.new("RGB", (dimension, dimension), "black")
box = Image.new("RGB", (20, 20), "red")

while y < side:
	while x < side:
		board.paste(box,(20*x + alt,20*y))
		x += 2
	x = 0
	if alt == 20:
		alt = 0
	else:
		alt = 20
	print("Current row:")
	print(y)
	y += 1

board.save("picture.png")