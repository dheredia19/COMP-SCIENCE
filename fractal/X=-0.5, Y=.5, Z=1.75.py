from PIL import Image
import sys
import time
from random import uniform

print("Julia Set Fractal Generator. Please enter values to generate the image.")

#xshift = input("X-Position Shift: ")
#yshift = input("Y-Position Shift: ")
#zoom = input("Zoom Level: ")

xshift = -0.5
yshift = .5
zoom = 1.75

try:
	xpos = float(xshift)
	ypos = float(yshift)
	zlevel = float(zoom)
	0/zlevel
except:
	print("Invalid parameters. Please check your values and try again.")
	quit()

xa = (-2.0 + xpos)/zlevel

xb = (2.0 + xpos)/zlevel
ya = (-2.0 + ypos)/zlevel
yb = (2.0 + ypos)/zlevel

imgx, imgy = 1024, 1024

maxIt = 256

image = Image.new("RGB", (imgx, imgy))

# Method from https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module [StackOverflow]
start_time = time.time()

try:
	for y in range(imgy):
		elapsed_time = time.time() - start_time
		# Method from (https://stackoverflow.com/questions/3002085/python-to-print-out-status-bar-and-percentage) [StackOverflow]
		row = (y/imgy)*20
		sys.stdout.write('\r')
		sys.stdout.write("[%-20s] %d%% (%d sec)" % ('='*int(row), (y/imgy)*100, elapsed_time))
		sys.stdout.flush()

		cy = y * (yb-ya) / (imgy - 1) + ya
		for x in range(imgx):
			cx = x * (xb-xa) / (imgx - 1) + xa
			z = complex(cx, cy)
			c = complex(-0.9495773349355123, -0.6144395610652076)
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 +c
			r = 255-i*20
			b = 255-(i*50)%maxIt
			g = 255-maxIt-i

			# sys.stdout.write("(" + str(cx) + "," + str(cy) + ")")
			# sys.stdout.write(str(r) + " | " + str(g) + " | " + str(b))
			'''sys.stdout.write('\r')
			sys.stdout.write("(" + str(int(cx)) + "," + str(int(cy)) + ")")
			sys.stdout.write(str(r) + " | " + str(g) + " | " + str(b))
			sys.stdout.flush()'''
			image.putpixel((x,y),(r,g,b))
except KeyboardInterrupt:
	sys.stdout.write('\r')
	sys.stdout.write("[%-20s] %d%% (%d sec)" % ('*'*int(row), (y/imgy)*100, elapsed_time))
	sys.stdout.write('\n')
	sys.stdout.write('\a')
	sys.stdout.flush()
	print("Operation cancelled.")
	quit()

sys.stdout.write('\r')
sys.stdout.write("[%-20s] %d%% (%d sec)" % ('='*20, 100, elapsed_time))
sys.stdout.write('\n')
sys.stdout.write('\a')
sys.stdout.flush()

print("Done!")
image.show()
