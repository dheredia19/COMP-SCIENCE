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

def save():
	destination = input("Name of File to Save (Leave Empty to Overwrite): ")
	if destination == "":
		save_path = sys.argv[1]
	else:
		save_path = destination

	start_time = time.time()

	print("Saving...")
	for y in range(imgy):
		elapsed_time = time.time() - start_time
		# Method from (https://stackoverflow.com/questions/3002085/python-to-print-out-status-bar-and-percentage) [StackOverflow]
		row = (y/imgy)*20
		sys.stdout.write('\r')
		sys.stdout.write("[%-20s] %d%% (%d sec)" % ('='*int(row), (y/imgy)*100, elapsed_time))
		sys.stdout.flush()
		for x in range(imgx):
			# Method from StackOverflow (https://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['red'] == 1:
				pixels[x,y] = (0, g, b)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['green'] == 1:
				pixels[x,y] = (r, 0, b)
			r, g, b = rgb_pic.getpixel((x, y))
			if options['blue'] == 1:
				pixels[x,y] = (r, g, 0)
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
				'''try:
					merge_list.append(temp_map[x-1,y-1])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x-1,y])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x-1,y+1])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x,y-1])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x,y+1])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x+1,y-1])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x+1,y])
				except IndexError:
					pass
				try:
					merge_list.append(temp_map[x+1,y+1])
				except IndexError:
					pass'''
				merge_rgb = tuple(merge_list)
				averages = [sum(index) / len(index) for index in zip(*merge_rgb)]
				for wonk in range(len(averages)):
					averages[wonk] = int(averages[wonk])
				pixels[x,y] = tuple(averages)
				'''blur = (0, 0, 0)
				count = 0
				try:
					blur += pixels[x-1,y-1]
					count += 1
				except:
					pass
				try:
					blur += pixels[x-1,y]
					count += 1
				except:
					pass
				try:
					blur += pixels[x-1,y+1]
					count += 1
				except:
					pass
				try:
					blur += pixels[x,y-1]
					count += 1
				except:
					pass
				try:
					blur += pixels[x,y+1]
					count += 1
				except:
					pass
				try:
					blur += pixels[x+1,y-1]
					count += 1
				except:
					pass
				try:
					blur += pixels[x+1,y]
					count += 1
				except:
					pass
				try:
					blur += pixels[x+1,y+1]
					count += 1
				except:
					pass

				blur = [element/count for element in blur]

				try:
					pixels[x-1,y-1] = blur
				except:
					pass
				try:
					pixels[x-1,y] = blur
				except:
					pass
				try:
					pixels[x-1,y+1] = blur
				except:
					pass
				try:
					pixels[x,y-1] = blur
				except:
					pass
				try:
					pixels[x,y+1] = blur
				except:
					pass
				try:
					pixels[x+1,y-1] = blur
				except:
					pass
				try:
					pixels[x+1,y] = blur
				except:
					pass
				try:
					pixels[x+1,y+1] = blur
				except:
					pass'''
			r, g, b = rgb_pic.getpixel((x, y))
			if options['sharp'] != 0:
				pass
			r, g, b = rgb_pic.getpixel((x, y))
			if options['bright'] != 0:
				pixels[x,y] = (r+options['bright'], g+options['bright'], b+options['bright'])
			r, g, b = rgb_pic.getpixel((x, y))
			if options['high'] != 0:
				if r+g+b > 381:
					pixels[x,y] = (r+options['high'], g+options['high'], b+options['high'])
			r, g, b = rgb_pic.getpixel((x, y))
			if options['shadow'] != 0:
				if r+g+b < 381:
					pixels[x,y] = (r+options['shadow'], g+options['shadow'], b+options['shadow'])
	rgb_pic.show()
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
		print(' |9| Save                 ')
		print(' |0| Exit                 ')
		print('\x1b[0m')
		try:
			choice = int(input("Choose a option: "))
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
			elif choice == 9:
				save()
			elif choice == 0:
				end()
			else:
				raise ValueError
		except ValueError:
			input("Invalid selection. Press [ENTER] to continue.")
			continue

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

try:
	menu()
except KeyboardInterrupt:
	print()
	end()
