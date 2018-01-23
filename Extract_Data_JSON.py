# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

    # Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_20285.json (Sum ends with 61)

# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# Data Format

# The data consists of a number of names and comment counts in JSON as follows:

'''
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
'''

# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

# Sample Execution

# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...

import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter location: ')
if len(address) < 1:
    address =  'http://py4e-data.dr-chuck.net/comments_20285.json'

uh = urllib.request.urlopen(address)
data = uh.read()
# Load the json data
info = json.loads(data)
# Print the length of the comments array
print('User count:', len(info['comments']))

sum = 0

# loop through each comments item
for item in info['comments']:
    # Grab the count
    notnumber = item['count']
    # Convert to integer and add to sum
    number = int(notnumber)
    sum += number
    print(number)
    #print('Count', item['comments']['count'])
print('Sum of comments is:', sum)
