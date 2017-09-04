'''
Created on Aug 7, 2017

@author: michel
'''
import json
import urllib.request
import urllib.parse
import urllib.error
count_sum = 0
#
#  http://py4e-data.dr-chuck.net/comments_10732.json
#
url = input("Enter the URL: ")
url_handle = urllib.request.urlopen(url)
print(url_handle)
print("================================================================================")
#
url_data = url_handle.read().decode()
print(url_data)

print("================================================================================")
#
js = json.loads(url_data)
print(js)
print("================================================================================")
print(type(js))
print("================================================================================")
#
js_pretty = json.dumps(js, indent=4)
print(js_pretty)
#

#
print("================================================================================")

list_dict = (js['comments'])
print(list_dict)

for item in list_dict:
    count = (item['count'])
    count_sum = count_sum + int(count)
print("Sum = ", count_sum)
