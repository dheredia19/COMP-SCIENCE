# http://effbot.org/imagingbook/image.htm

from PIL import Image
import os
import random

print("If you want to be Picasso, we've gotta show you an example, first.")
pixels = input("In order to do that, you gotta tell me how many pixels you want per side! ")
lines = input("Now that we've got that, how many lines should be drawn? ")

try:
	dimension = int(pixels)
	draws = int(lines)
except:
	print("I need numbers, you dummy! You'll never be good at chess at this rate...")
	quit()

canvas = Image.new("RGB", (dimension, dimension), "black")

for progress in range(draws):
	for coord in range(dimension):
		canvas.putpixel((coord,random.randint(0,dimension)),(66,134,244))

canvas.save("lines.png")