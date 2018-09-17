import time

print("Hi, stranger! Hope you're having a good day.")
time.sleep(3)
weather = input("Well, do you mind telling me what the weather's like today? I don't know whether or not to bring out my umbrella... ")

if "sun" in weather:
	print("Awesome! Maybe I'll put my shorts on!")
elif "cloud" in weather:
	print("That's not too bad. I suppose I'll take my jacket.")
elif "rain" in weather:
	print("Well, shucks. Better bring it, then!")
elif "snow" in weather:
	print("Yikes...better bring out my boots, as well.")
elif "hurricane" in weather:
	print("Holy cow! Might as well stay inside!")
elif "tornado" in weather:
	print("Wow, better duck and cover before it comes!")
else:
	print("Well, that wasn't particularly helpful.")