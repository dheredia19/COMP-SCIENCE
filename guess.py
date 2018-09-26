import random

mine = random.randint(1,10)

print("Guess my number, or not. I don't care...")

def goback():
	guess = int(input())
	if guess == mine:
		print("Wow, smartypants, you did it. Now go away.")
		quit()
	else:
		print("Wrong! Of course you're wrong. I'm not surprised.")
		if guess < mine:
			print("Hint: my number is higher than your guess.")
		else:
			print("Hint: my number is lower than your guess.")
		goback()
goback()