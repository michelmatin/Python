'''
Created on Aug 4, 2017

@author: michel
'''
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter the position in the list of achor tags
pos_str = input("Enter the position: ")
pos = int(pos_str)
#
# enter how many times to run the sequence
count_str = input("Enter the count: ")
count = int(count_str)
counter = 1

url = input('Enter the first URL: ')

# First count
while counter <= count:
    counter = counter + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
# print(tags)
 #   print(tags[pos - 1])
    print(tags[pos - 1].get('href', None))
    url = (tags[pos - 1].get('href', None))

# Second count
#html = urllib.request.urlopen(url_1, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup('a')
# print(tags)
#print(tags[pos - 1])
#print(tags[pos - 1].get('href', None))
#url_2 = (tags[2].get('href', None))

# for tag in tags:
#   new_url = (tag.get('href', None))
#   print(new_url)
