'''
Created on Aug 9, 2017

@author: michel
'''
import json
import urllib.request
import urllib.parse
import urllib.error

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# input =  = South Federal University
#
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input("Please enter the location: ")
url = serviceurl + \
    urllib.parse.urlencode({'sensor': 'false', 'address': address})

print('retrieving http://', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#
print(urllib.request.urlopen(url).read().decode())

print("=====================================================================")
print("DATA")
print(type(data))
print(data)
print("=====================================================================")
#
print(repr(data))
#
print("=====================================================================")

js = json.loads(data)
print('JSON DUMP')
print(json.dumps(js, indent=4))
#
print("=====================================================================")
#
list_dict = (js['results'])
print(list_dict)
# print(list_dict['place_id'])

for item in list_dict:
    print(item)
    id = item["place_id"]
print('Place id', id)
