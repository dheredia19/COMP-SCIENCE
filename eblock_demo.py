import time # For delay function

# Initiate opening sequence
name = input("Greetings! What is your name? ")
print("Nice to meet you, " + name +". I must ask you an important question. ")
time.sleep(3) # Dramatic pause

wallet = input("What's in your wallet? ") # Get user input

# Input processing section
if 'money' in wallet:
    contents = "money"
elif 'dollar' in wallet:
    contents = "money"
elif 'card' in wallet:
    contents = "card"
elif 'id' in wallet:
    contents = "ID"
elif 'ID' in wallet:
    contents = "ID"
elif 'cash' in wallet:
    contents = "cash"
else:
	# The user has nothing that matches the criteria, jump out of execution
	print("You are useless to me. Goodbye.")
	input("Press Enter to continue...") # Pause before program closes
	quit()

print("I'm afraid you must hand the " + contents + " over within 30 seconds. Otherwise, your computer will explode.")