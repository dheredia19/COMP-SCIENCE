# http://effbot.org/imagingbook/image.htm

from PIL import Image
import os

print("We're going to make a checkerboard so I can kick your behind at chess.")
squares = input("In order to do that, you gotta tell me how many squares you want per side! ")
pixels = input("Now that we've got that, how many pixels should each square be? ")

try:
	side = int(squares)
	size = int(pixels)
except:
	print("I need numbers, you dummy! You'll never be good at chess at this rate...")
	quit()

dimension = side * size
x = y = 0
alt = size
number = range(0,side)
print(number)

board = Image.new("RGB", (dimension, dimension), "black")
box = Image.new("RGB", (size, size), "red")

while y < side:
	while x < side:
		board.paste(box,(size*x + alt,size*y))
		x += 2
	x = 0
	if alt == size:
		alt = 0
	else:
		alt = size
	print("Current row:")
	print(y)
	y += 1

board.save("picture.png")