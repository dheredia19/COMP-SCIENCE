import sys

print("Welcome to the Super Duper Wind Chill Figureouternator.")

t = sys.argv[1]
v = sys.argv[2]

print("Detected arguments:")
print("Temperature: " + str(t) + " °F")
print("Wind speed: " + str(v) + " MPH")

t = float(t)
v = float(v)

w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16

print("Wind chill: " + str(w) + " °F")