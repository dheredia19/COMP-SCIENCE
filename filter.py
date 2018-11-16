from PIL import Image
import time
import sys
import os

def clear(): 
	# for windows 
	if os.name == 'nt':
		_ = os.system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = os.system('clear')

options = {
  "red": 0,
  "green": 0,
  "blue": 0,
  "blur": 0,
  "sharp": 0,
  "bright": 0,
  "high": 0,
  "shadow": 0
}

def save(copy = 0):
	if copy == 1:	
		destination = input("Name of File to Save (Leave Empty to Overwrite): ")

	start_time = time.time()

	print("Processing...")
	for y in range(imgy):
		elapsed_time = time.time() - start_time
		# Method from (https://stackoverflow.com/questions/3002085/python-to-print-out-status-bar-and-percentage) [StackOverflow]
		row = (y/imgy)*20
		sys.stdout.write('\r')
		sys.stdout.write("[%-20s] %d%% (%d sec)" % ('='*int(row), (y/imgy)*100, elapsed_time))
		sys.stdout.flush()
		for x in range(imgx):
			# Focus Modifiers (must come first to not corrupt other edits)
			# Method from StackOverflow (https://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['blur'] != 0:
				# Method from StackOverflow (https://stackoverflow.com/questions/12412546/average-tuple-of-tuples)
				temp_map = pixels
				merge_list = []
				for y_blur in range(0-options['blur'],1+options['blur']):
					for x_blur in range(0-options['blur'],1+options['blur']):
						try:
							merge_list.append(temp_map[x+x_blur,y+y_blur])
						except IndexError:
							pass
				merge_rgb = tuple(merge_list)
				averages = [sum(index) / len(index) for index in zip(*merge_rgb)]
				for wonk in range(len(averages)):
					averages[wonk] = int(averages[wonk])
				pixels[x,y] = tuple(averages)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['sharp'] != 0:
				# Method from StackOverflow (https://stackoverflow.com/questions/12412546/average-tuple-of-tuples)
				temp_map = pixels
				split_list = []
				for y_sharp in range(-1,2):
					for x_sharp in range(-1,2):
						try:
							difference = tuple(x-y for x, y in zip(temp_map[x+x_sharp,y+y_sharp], temp_map[x,y]))
							combined = sum(difference)/3
							finished = abs(combined)
							#print(difference, combined, finished)
							if finished > options['sharp']:
								pixels[x,y] = (255, 255, 255)
						except IndexError:
							pass
			# Intensity Modifiers (must come before color muting to change original values)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['bright'] != 0:
				pixels[x,y] = (r+options['bright'], g+options['bright'], b+options['bright'])
			r, g, b = rgb_pic.getpixel((x, y))
			if options['high'] != 0:
				if r+g+b > 450:
					amount  = int(((r+g+b - 450)/315)*options['high'])
					pixels[x,y] = (r+amount, g+amount, b+amount)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['shadow'] != 0:
				if r+g+b < 300:
					amount  = int(((r+g+b - 450)/315)*options['high'])
					pixels[x,y] = (r+amount, g+amount, b+amount)
			# Color Modifiers (must come last after all edits to pixels)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['red'] == 1:
				pixels[x,y] = (0, g, b)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['green'] == 1:
				pixels[x,y] = (r, 0, b)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['blue'] == 1:
				pixels[x,y] = (r, g, 0)
	if copy == 0:
		pass
	else:
		if destination == "":
			rgb_pic.save(sys.argv[1])
		else:
			rgb_pic.save(destination)
	rgb_pic.show()
	#img.show()

	print()
	end()

def end():
	print("Exiting...")
	quit()

def menu():
	while True:
		clear()
		print('\x1b[6;30;42m')
		print('__________________________')
		print(' Adobe Pythoshop Express® ')
		print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
		print(' |1| Mute Red Channel   ', end='')
		print('* ') if options['red'] == 1 else print('  ')
		print(' |2| Mute Green Channel ', end='')
		print('* ') if options['green'] == 1 else print('  ')
		print(' |3| Mute Blue Channel  ', end='')
		print('* ') if options['blue'] == 1 else print('  ')
		print('--------------------------')
		print(' |4| Apply Blur         ', end='')
		print('* ') if options['blur'] != 0 else print('  ')
		print(' |5| Apply Sharpness    ', end='')
		print('* ') if options['sharp'] != 0 else print('  ')
		print('--------------------------')
		print(' |6| Adjust Brightness  ', end='')
		print('* ') if options['bright'] != 0 else print('  ')
		print(' |7| Adjust Highlights  ', end='')
		print('* ') if options['high'] != 0 else print('  ')
		print(' |8| Adjust Shadows     ', end='')
		print('* ') if options['shadow'] != 0 else print('  ')
		print('--------------------------')
		print(' |P| Preview              ')
		print(' |S| Save                 ')
		print(' |R| Reset                ')
		print(' |Q| Quit                 ')
		print('\x1b[0m')
		get_user = input("Choose a option: ")
		get_user = get_user.lower()
		try:
			choice = int(get_user)
			if choice == 1:
				options['red'] = 1 - options['red']
			elif choice == 2:
				options['green'] = 1 - options['green']
			elif choice == 3:
				options['blue'] = 1 - options['blue']
			elif choice == 4:
				options['blur'] = int(input("Effect amount: "))
			elif choice == 5:
				options['sharp'] = int(input("Effect amount: "))
			elif choice == 6:
				options['bright'] = int(input("Effect amount: "))
			elif choice == 7:
				options['high'] = int(input("Effect amount: "))
			elif choice == 8:
				options['shadow'] = int(input("Effect amount: "))
			else:
				raise ValueError
		except ValueError:
			if get_user == "p":
				save()
			elif get_user == "s":
				save(1)
			elif get_user == "r":
				reset()
			elif get_user == "q":
				reset()
				end()
			else:
				input("Invalid selection. Press [ENTER] to continue.")
			continue


def reset():
	global options
	remove = input("Discard changes? ")
	if "y" in remove:
		options = dict.fromkeys(options, 0)
	else:
		menu()

if len(sys.argv) < 2:
	print("No input file detected!")
	end()

try:
	temp_pic = Image.open(sys.argv[1])
	# Method from StackOverflow (https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil)
	rgb_pic = temp_pic.convert('RGB')
	imgx, imgy = rgb_pic.size
	#https://stackoverflow.com/questions/36468530/changing-pixel-color-value-in-pil
	pixels = rgb_pic.load()
except FileNotFoundError:
	print("Input file not found!")
	end()
except OSError:
	print("Input file is invalid!")
	end()

try:
	menu()
except KeyboardInterrupt:
	print()
	end()
