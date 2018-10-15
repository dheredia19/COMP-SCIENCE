import sys

n = int(sys.argv[1])
left = True

def moves(n, left):
	if n == 0:
		return
	moves(n-1, not left)
	if left:
		print(str(n) + ' was moved left.')
	else:
		print(str(n) + ' was moved right.')
	moves(n-1, not left)

moves(n, left)