import time

name = input("Greetings! What is your name? ")
print("Nice to meet you, " + name +". I must ask you an important question. ")
time.sleep(3)
wallet = input("What's in your wallet? ")

if wallet.casefold().find("money") == -1:
    contents = "money"
elif wallet.casefold().find("card") == -1:
    contents = "card"
elif wallet.casefold().find("id") == -1:
    contents = "ID"
elif wallet.casefold().find("cash") == -1:
    contents = "cash"
elif wallet.casefold().find("dollar") == -1:
    contents = "dollar"
elif wallet.casefold().find("dollars") == -1:
    contents = "dollars"
else:
	print("You are useless to me. Goodbye.")
	input("Press Enter to continue...")
	quit()

print("I'm afraid you must hand the " + contents + " over within 30 seconds. Otherwise, your computer will explode.")

if "cash" in wallet:
