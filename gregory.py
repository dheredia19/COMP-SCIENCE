import sys

print("You have stumbled upon a program that converts a date to a day of the week.")

m = sys.argv[1]
d = sys.argv[2]
y = sys.argv[3]

print("Detected arguments:")
print("Month: " + m)
print("Day: " + d)
print("Year: " + y)

m = int(m)
d = int(d)
y = int(y)

my = (14 - m)/12

yo = (y - (14 - m))/12
x = yo + yo/4 - yo/100 + yo/400
mo = m + 12*(my) - 2
dy = (d + x + (31*mo)/12)
do = dy % 7
day = int(do)

print("my: " + str(my))
print("yo: " + str(yo))
print("x: " + str(x))
print("mo: " + str(mo))
print("dy: " + str(dy))
print("do: " + str(do))
print("day: " + str(day))

if day == 0:
	print("It's Thursday, my dudes!")
if day == 1:
	print("It's Friday, my dudes!")
if day == 2:
	print("It's Saturday, my dudes!")
if day == 3:
	print("It's Sunday, my dudes!")
if day == 4:
	print("It's Monday, my dudes!")
if day == 5:
	print("It's Tuesday, my dudes!")
if day == 6:
	print("It's Wednesday, my dudes!")