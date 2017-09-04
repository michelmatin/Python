'''
Created on Aug 5, 2017

@author: michel
'''
import urllib.request
import urllib.parse
import urllib.error
import ssl
import xml.etree.ElementTree as ET
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")


xml = urllib.request.urlopen(url, context=ctx).read()
print(xml)

tree = ET.fromstring(xml)
print(tree)
print("Note:", tree.find('note').text)

list_count = tree.findall('comments/comment')
print(list_count)
for comment in list_count:
    print("count: ", comment.find("count").text)
    count = comment.find("count").text
 #   print(int(count))
    sum = sum + int(count)

print("Sum = ", sum)
