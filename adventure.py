'''
*** A Royal Rendezvous ***
Completed on September 24, 2018 by Daniel Heredia
An Interactive Story
Code Exerpts from StackOverflow, GeeksForGeeks
On my honor, I have neither given or received unauthorized aid.
'''

import sys # gives us access to system related methods

# This block of code saves an CLI argument to a variable if present, or ignores it if it isn't.
try:
	mode = sys.argv[1]
except IndexError:
	mode = "none"
	pass

# ----- STATISTICS -----
# (saves all game progress)

# These check if you've been somewhere.
bedroom_get = 0
street_get = 0
business_get = 0
clothing_get = 0
hill_get = 0
castle_front_get = 0

# These check if you've interacted with something.
newspaper = 0
suit = 0

# These check if you've completed a part of the game.
act1 = 0

# ----- FUNCTIONS -----
# (defines basic game functionality)

# define our clear function (GeeksForGeeks) [https://www.geeksforgeeks.org/clear-screen-python/]
# import only system from os 
from os import system, name
def clear(): 
	# for windows 
	if name == 'nt':
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear')

# define the quit menu ***currently does not fully work because it is called as a result of an Exception***
def endgame():
	print("quit")
	end = input("Are you sure you want to quit? ")
	if "y" in end:
		quit()
	else:
		pass # ***program ends up exiting here, instead of returning to previous function***

# define the info screen, only used if called by CLI
def info():
	print("Hi. Welcome to the information page, where you will learn about the game and its intricacies.")
	print('If you are looking for help how to play the game, you can type "help" at the prompt once you are inside.')
	print("At any point, you may press ENTER to exit.")
	print("")
	print("Anyways, let's get right to it. The premise of the game is that you, the poor but resourceful protaganist, have a relatively hard-knock life and you are spontaneously smitten with the princess of your kingdom.")
	print("By spending what little money you have at the shops at your town and befriending a homeless person, you manage to make it to the castle to find the princess.")
	print("With what you gained earlier, you manage to break into the castle and find the princess' room. She, understandably, is beyond freaked out. She has never met a commoner before, but soon confides in you about the boring life of being royalty.")
	print("You agree that in exchange for her hand in marriage, you will bust her out of the castle to lead a fun and exciting life. You two manage to get out of the castle and run through the town to the neighboring kingdom.")
	print("Unfortunately (but also understandably), her father is beyond enraged. He knows nothing about the wearabouts of his daughter, and sets out with his army to track her down.")
	print("Meanwhile, you are detained in the neighboring kingdom for not having a visa, but the king of that kingdom recognizes the princess and takes you both in to his fort.")
	print("At this point in time, the father finds out that you and the princess retreated to this neighboring kingdom and sets out for you both.")
	print("The army swarms the fort in which you are all taking residence, and the father demands that his daughter is returned.")
	print("However! We learn some very important details about both of the leaders. 1) They are brothers, and actually fraternal twins, but 2) the king of the neighboring kingdom was exiled by his brother because he was homosexual.")
	print("The king who is keeping you safe proclaims that you both will not be returned unless his brother finally accepts him for who he is. After some deliberation, the princess' father realizes how foolish he had been all this time, and thanked his brother for keeping his daughter safe.")
	print("The princess, who had fallen in love with you during all that drama, insisted that her father let her marry you, and he agreed.")
	input("The End. Press ENTER to exit the program.")
	quit()

def howto():
	clear()
	print("******* HELP DOCUMENT *******")
	print("There are a few primary methods of control for your textual character.")
	print("")
	print("*** TYPING CONVENTIONS ***")
	print("The command parser only takes one argument at a time. All arguments are predefined in the code, so if an action does not work, try a synonymous action.")
	print("")
	print("*** CARDINAL DIRECTIONS ***")
	print('These are the primary way to get around in this game. You can type "north", "south", "east", or "west". Other directions include "up" or "down", in special circumstances.')
	print("")
	print("*** ACTIONS ***")
	print('Other than directional inputs, you can use English verbs to choose what to do, such as "open" or "exit".')
	print("")
	print("*** INTERACTIONS ***")
	print('Many items and people in the virtual world can be interacted with just by saying what it is, like opening the "dresser" or picking up the "newspaper".')
	print("")

# ----- LOCATIONS -----
# (defines location sequences)

# Game Introdution
def beginning():
	print("Please note that game is rated as PG-13. The developer apologizes profusley for any profanities or vulgarities contained within this program.")
	input("That being said, we can discuss who YOU are. After each text prompt, hit the ENTER key to advance the program.")
	input("You are a lower-class peddler living of the kingdom of Nothingham. You have great fun doing what you do for a living, but it is hard work and you want to have more fun.")
	bedroom()

# First Location: Bedroom
def bedroom():
	print("You are in the bedroom.")
	global bedroom_get # Pulls in global variable into function
	if bedroom_get == 0: # Checks if function has been accessed before
		print("Your room, built within your small, tenement apartment, has a small dresser with ratty clothes. Pushed up against your bed, on which you've awaken from, there is not much standing room. That detail matters little, as you have few house guests and you are working constantly.")
		print("There is a door to the east that opens to stairs down to the street.")
		bedroom_get += 1 # Sets function access state
	entry = input("> ") # Stores user input to be tested
	if "east" in entry:
		print("You open the door and walk down the stairs out onto the street.")
		street()
	if "door" in entry:
		print("You open the door and walk down the stairs out onto the street.")
		street()
	if "dresser" in entry:
		print("You pull out one of the drawers of your dresser. You find a small note that reads:")
		print('"THIS IS A BETA VERSION. SOME FEATURES ARE NOT IMPLEMENTED."')
	elif "exit" in entry:
		print("You open the door and walk down the stairs out onto the street.")
		street()
	elif "down" in entry:
		print("You open the door and walk down the stairs out onto the street.")
		street()
	elif "open" in entry:
		print("You open the door and walk down the stairs out onto the street.")
		street()
	elif "look" in entry:
		bedroom_get = 0 # Resets function access state for description to be reprinted
	elif "clear" in entry:
		clear() # Clears screen using custom function
	elif "help" in entry:
		howto() # Opens help screen for the game
	else:
		print("That doesn't work here.")
	bedroom()

# Second Location: Street
def street():
	print("You are on the street by your house.")
	global street_get
	if street_get == 0:
		print("The avenue on which you live on, filthy and rat-ridden, leads through the town's main business district. Further north the path, there are various shops that line the street. You can see the kingdom's castle in the distance. In the other direction, the road leads south to the drawbridge to the neighboring kingdom.")
		print("The stairs to your apartment are to the west.")
		street_get += 1
	entry = input("> ")
	if "west" in entry:
		print("You walk up the stairs into your apartment.")
		bedroom()
	elif "up" in entry:
		print("You walk up the stairs into your apartment.")
		bedroom()
	elif "north" in entry:
		print("You walk up the street towards the town center.")
		business()
	elif "south" in entry:
		print("You walk down the steet towards the river.")
		if act1 == 0:
			print("When you reach the drawbridge, a guard steps in front of you.")
			print('"HALT! DO YOU HAVE IDENTIFICATION OF YOUR CREDENTIALS?"')
			print("You are so shaken that you simply shake your head and turn back.")
		else:
			bridge()
	elif "look" in entry:
		street_get = 0
	elif "clear" in entry:
		clear()
	elif "help" in entry:
		howto()
	else:
		print("That doesn't work here.")
	street()

# Third Location: Business District
def business():
	print("You are in the business district.")
	global business_get
	if business_get == 0:
		print("Walking through this part of town never fails to make you gag. The hustle and bustle of people fills your ears with its distinct pandemonium. Shops line the street, but your stand for selling small wears is the business you call your own. To the west, you see a candy store, and to the east, you see a clothing store.")
		print("The street of your apartment is to the south, and the way to the castle is to the north.")
		business_get += 1
	entry = input("> ")
	if "north" in entry:
		print("You continue along the road towards the castle.")
		hill()
	elif "south" in entry:
		print("You continue down towards your apartment.")
		street()
	elif "east" in entry:
		print("You walk inside the establishment.")
		clothing()
	elif "west" in entry:
		print("You walk towards the candy store, but the windows are boarded up with a small sign hanging on the door. It reads:")
		print('"NOT IMPLEMENTED IN BETA VERSION"')
	elif "look" in entry:
		business_get = 0
	elif "clear" in entry:
		clear()
	elif "help" in entry:
		howto()
	else:
		print("That doesn't work here.")
	business()

# Branch Location: Clothing Store
def clothing():
	print("You are inside the clothing store.")
	global clothing_get
	global suit
	if clothing_get == 0:
		print("The shelves and carts are lined with all sorts of clothing styles. Traditionally, you have not been able to afford much of the options here, but you have never needed to anyways. A woman stands at the cash register, eagerly waiting for your purchase.")
		print("The exit door is to the west.")
		clothing_get += 1
	entry = input("> ")
	if "west" in entry:
		print("You walk out the door to the street.")
		business()
	if "door" in entry:
		print("You walk out the door to the street.")
		business()
	if "exit" in entry:
		print("You walk out the door to the street.")
		business()
	elif "talk" in entry:
		if suit != 0:
			print("You already have new clothing!")
		else:
			print("You say hello to the woman at the register. She smiles and walks towards you.")
			input('"Welcome to my clothing boutique! I assume you are in need of some new threads, based on your current attire..." You roll your eyes at her and say that you want the cheapest suit they have.')
			input('"Well, if a designer brand is out of the question, then how about some items on clearance, then?"')
			input('She brings you into the back of the store and opens a large chest. The room has an almost unbearable stench of mothballs and decaying fabric. The woman goes through multiple clothes in the chest and pulls out an ivory suit that is just about your size. "This should do it, for what you\'re looking for."')
			input('You ask for the price, but she laughs and says, "Oh, you wouldn\'t be able to afford this at retail. I\'ve been trying to get rid of this for the longest time! Let\'s just say you owe me a favor, okay?"')
			print("You are now holding a suit.")
			suit += 1
	elif "buy" in entry:
		if suit != 0:
			print("You already have new clothing!")
		else:
			print("You say hello to the woman at the register. She smiles and walks towards you.")
			input('"Welcome to my clothing boutique! I assume you are in need of some new threads, based on your current attire..." You roll your eyes at her and say that you want the cheapest suit they have.')
			input('"Well, if a designer brand is out of the question, then how about some items on clearance, then?"')
			input('She brings you into the back of the store and opens a large chest. The room has an almost unbearable stench of mothballs and decaying fabric. The woman goes through multiple clothes in the chest and pulls out an ivory suit that is just about your size. "This should do it, for what you\'re looking for."')
			input('You ask for the price, but she laughs and says, "Oh, you wouldn\'t be able to afford this at retail. I\'ve been trying to get rid of this for the longest time! Let\'s just say you owe me a favor, okay?"')
			print("You are now wearing a suit.")
			suit += 1
	elif "look" in entry:
		clothing_get = 0
	elif "clear" in entry:
		clear()
	elif "help" in entry:
		howto()
	else:
		print("That doesn't work here.")
	clothing()

# Fourth Location: Top of the Hill
def hill():
	print("You are on the top of a steep hill.")
	global hill_get
	if hill_get == 0:
		print("Along this part of the road, the pavement of the city gives way to gravely dirt towards the castle. Being on the outskirts of the town, the only buildings around are part of the farmland with large, green pastures.")
		if act1 == 0:
			print("To the side of the path, you see a homeless man with a small tent with a fire going.")
		else:
			print("To the side of the path, you see a small tent with the remenants of a fire. The homeless man is gone.")
		print("Your town is to the south, and the castle is just north from where you are standing.")
		hill_get += 1
	entry = input("> ")
	if "north" in entry:
		print("You walk along the path towards the castle.")
		castle_front()
	elif "south" in entry:
		print("You walk towards the center of town.")
		business()
	elif "talk" in entry:
		print("You say hello to the homeless man, but he barks at you before you can continue.")
		print('"Can\'t you read the sign?"')
		print("You walk over to look at the sign hanging on the opening of his tent. It reads:")
		print('"NOT IMPLEMENTED IN BETA VERSION"')
	elif "tent" in entry:
		print("You walk over to the small tent by the path, but there is a small sign hanging of it that reads:")
		print('"NOT IMPLEMENTED IN BETA VERSION"')
	elif "look" in entry:
		hill_get = 0
	elif "clear" in entry:
		clear()
	elif "help" in entry:
		howto()
	else:
		print("That doesn't work here.")
	hill()

# Fifth Location: Front of Castle
def castle_front():
	print("You are standing in front of your kingdom's castle.")
	global castle_front_get
	global suit
	if castle_front_get == 0:
		print("The castle towers over you like a skyscraper, standing at about 15 stories high. Constructed with a stone facade, it appears fortified from all angles from attack and intruders. There is a large set of doors guarded by two armored men to the north, and paths that lead around the building to the east and west.")
		print("The path towards your town is to the south.")
		castle_front_get += 1
	entry = input("> ")
	if "north" in entry:
		print("You walk towards the doors, but the guards step forward to block your next step.")
		if suit != 0:
			print('"HALT! ARE YOU HERE FOR AN OFFICIAL TOUR OF THE CASTLE?"')
			input("You pause for a moment, trying to understand what the guard means by his question.")
			print('"WELL, I HAVEN\'T ALL DAY, YOU KNOW. IF YOU\'RE HERE FOR THE TOUR, YOU TAKE THE TEST."')
			input("You continue to stare blankly at him for another beat before he breaks in again.")
			print('"WELL, SINCE YOU\'RE SO CLUELESS, YOU\'RE MOST LIKELY TO FAIL. BUT HERE GOES, ANYWAYS. ARE YOU READY?"')
			test = input("-> ")
			if "y" in test:
				print('"ALRIGHTY THEN. LET US BEGIN. QUESTION 1: WHAT IS THE ROYAL PRINCESS\' FAVORITE COLOR?"')
				color = input("-> ")
				if "purple" in color:
					print('"WELL, THEN! WHAT A SURPRISE! YOU ACTUALLY KNOW SOMETHING ABOUT SOMETHING. VERY WELL, QUESTION 2: WHAT WAS HERE ON THIS LAND BEFORE OUR NOBLE KING SET FOOT UPON IT YEARS AGO?')
					land = input("-> ")
					if "nothing" in land:
						print('"ANOTHER SHOCKER FROM THE VISITOR! HOWEVER, YOU MIGHT HAVE JUST BEEN GUESSING. THUS, WE HAVE QUESTION 3: WHAT IS THE QUEEN\'S FAVORITE NUMBER?"')
						try:
							number = int(input("-> "))
						except ValueError:
							print('"I DON\'T HAVE TIME FOR YOUR NONSENSE. GO AWAY!"')
							castle_front()
						if number == 4:
							print('"GOLLY! I\'M OUTSTANDED! COMMONERS RARELY MAKE IT THIS FAR. I SUPPOSE WE SHOULD GIVE YOU A TOUR, THEN."')
							input("The guards open the doors to the castle and you follow them inside.")
							print("") # whitespace
							print("*******END OF ACT 1*******")
							print("Thank you for playing this game! Acts 2 and 3 are not included in the BETA version, but will be coming out soon.")
							input("Press ENTER to exit the program.")
							quit()
						else:
							print('"HA! IT IS CLEAR YOU WERE GUESSING, BASED ON YOUR WRONG ANSWER. NOW GO AWAY!"')
					else:
						print('"INCORRECT! WHY, THAT IS ONE OF THE MOST BASIC FACTS IN THE BOOK! NOW GO AWAY!"')
				else:
					print('"WRONG! IT WAS OBVIOUS YOU HADN\'T A CLUE. NOW GO AWAY!"')
			elif "n" in test:
				print('"HA! I\'M NOT SURPRISED. NOW GO AWAY!"')
			else:
				print('"I DON\'T HAVE TIME FOR YOUR NONSENSE. GO AWAY!"')
		else:
			print('"HALT! TRASHY COMMONERS ARE NOT PERMITTED TO ENTER THE CASTLE. GO AWAY!"')
	elif "south" in entry:
		print("You walk up the hill towards the town.")
		hill()
	elif "east" in entry:
		print("")
	elif "west" in entry:
		print("")
	elif "look" in entry:
		castle_front_get = 0
	elif "clear" in entry:
		clear()
	elif "help" in entry:
		howto()
	else:
		print("That doesn't work here.")
	castle_front()

# -----GAME PROCEEDURE SECTION-----
# (proceedurally runs through all code present)

try: # This is the second "try an catch" sequence. This quietly exits the game if Ctrl-C is pressed during the exit menu.
	try: # Technically, this is the first "try and catch" sequence. Catches a Ctrl-C from crashing the game.
		# This conditional checks for the "debug" CLI argument from earlier.
		if "debug" in mode:
			# define the top level module (StackOverflow) [https://stackoverflow.com/questions/8706309/how-to-reference-to-the-top-level-module-in-python-inside-a-package]
			top_package = __import__(__name__.split('.')[0])
			location = input("You are now in debug mode. Please enter a location or a statistic: ")
			# call the specified function (StackOverflow) [https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string]
			method_to_call = getattr(top_package, location)
			result = method_to_call()
		elif "info" in mode:
			clear()
			info()
		print("You are about to embark on a delicious and scrumptious journey of love.")
		start = input("Are you ready to begin? ")
		if "y" in start:
			print("Let's jump to it!")
			input("Press ENTER to continue.") # Dummy input function, just to make excecution a little more interactive.
			clear() # Clears the screen.
			beginning() # Starts the game sequence.
			print("Hello, stranger. If you see this, you lose the game. Sorry, no refunds.") # This would only appear if something went horrifically wrong.
		elif "n" in start:
			print("Well, that's a darn shame.")
		else:
			print("I couldn't understand that. I assume you mean 'no'.") # Sad.
	except KeyboardInterrupt:
		endgame()
except KeyboardInterrupt:
	quit()