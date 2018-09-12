import sys # Call system functions

print("Hello ", end='') # Begin greeting string

for x in range(1, len(sys.argv)): # Assess number of arguments
	if x == len(sys.argv)-1: # If parser reaches the last argument
		if len(sys.argv) != 2: # No conjunction needed for one name, catch exception
			print("and ", end='') # Print an "and"
	print(sys.argv[x], end='') # Get the name from argument
	if x == len(sys.argv)-1: # If parser reaches the last argument
		print("!", end='') # Print an exclamation point
		quit() # Stop execution
	else: # If parser does not reach the last argument
		if len(sys.argv) != 3: # No comma needed for two names, catch exception
			print(", ", end='') # Print a comma
		else: # Space still needed for names
			print(" ", end='') # Print a comma