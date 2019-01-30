'''
Requests HTTP Library: Real-World Demonstration
To get a sense of what using this library is like, this file shows
a relatively versatile demo script that downloads a table stored in
Comma-Seperated Values, interprets the file into a Python object,
and generates a goregeous graph out of the data in boxplot form.

'''

# Prerequesits for the demo
import requests
import csv
import matplotlib.pyplot as plt

# Get the stuff
url = 'https://pdtortoise.ddns.net/_h5ai/daphniasurvivors.csv'
r = requests.get(url) # Makes GET request to server
download = r.text.splitlines() # Stores server data to variable in STRING format

# Process the stuff
reader = csv.reader(download) # Converts CSV format into nested lists
labels = [] # Prepare for storing x-axis labels
data = [] # Prepare for storing y-axis values
values = list(reader) # Convert CSV object to standard object
for row in values:
	try:
		place = labels.index(row[0]) # Check if grouping is created
		data[place].append(row[1]) # If present, add the value
	except ValueError: # ValueError if not found
		labels.append(row[0]) # Add new x-axis label
		temp = [row[1]] # Temporary 1-element list
		data.append(temp) # Added to data as a new grouping

# Show the stuff
print(data) # Check if array contains all data!
for i,x in enumerate(data):
	if x[0].isdigit() != 1: # Test if list element is not a number
		data.pop(i) # Get rid of the offending value
		labels.pop(i)  # Remove the label associated with it
data = [[int(i) for i in x] for x in data] # Make everything numeric before graphing
plt.boxplot(data, labels=labels) # Creates a boxplot with the given data
plt.savefig('plot.png') # Saves graph as file
