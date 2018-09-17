import sys
import math

print("I will continuously compound your interest until your pockets swell with cash!")

P = sys.argv[1]
r = sys.argv[2]
t = sys.argv[3]

print("Detected arguments:")
print("Principal amount: $" + P)
print("Annual interest rate: " + r)
print("Time: " + t + " years")

P = float(P)
r = float(r)
t = float(t)

M = P*math.exp(r*t)

M = str(M)

print("Resulting money: $" + M + "!")