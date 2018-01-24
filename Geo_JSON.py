# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

# http://py4e-data.dr-chuck.net/geojson?

# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.

# To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py

# Test Data / Sample Execution

# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

# $ python3 solution.py
# Enter location: South Federal UniversityRetrieving http://...
# Retrieved 2101 characters
# Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# Use this static subset API with no rate limits
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    # Get user input
    address = input('Enter location: ')
    if len(address) < 1: break

    # Append user input to serviceurl
    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    # Open  and decode and print length
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # Try to load JSON data
    try:
        js = json.loads(data)
    except:
        js = None

    # Conditional if noting was retrieved from API
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Print what was retrieved
    print(json.dumps(js, indent=4))

    #lat = js["results"][0]["geometry"]["location"]["lat"]
    #lng = js["results"][0]["geometry"]["location"]["lng"]
    #print('lat', lat, 'lng', lng)
    #location = js['results'][0]['formatted_address']
    location = js['results'][0]['place_id']
    print(location)
