import sys

print("Hello ", end='')

for x in range(1, len(sys.argv)):
	if x == len(sys.argv)-1:
		print("and ", end='')
	print(sys.argv[x], end='')
	if x == len(sys.argv)-1:
		print("!", end='')
		quit()
	else:
		print(", ", end='')