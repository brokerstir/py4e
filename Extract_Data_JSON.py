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

import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter location: ')
if len(address) < 1:
    address =  'http://py4e-data.dr-chuck.net/comments_20285.json'

uh = urllib.request.urlopen(address)
data = uh.read()
info = json.loads(data)
print('User count:', len(info['comments']))

sum = 0

for item in info['comments']:
    notnumber = item['count']
    number = int(notnumber)
    sum += number
    print(number)
    #print('Count', item['comments']['count'])
print('Sum of comments is:', sum)
