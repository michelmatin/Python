'''
Created on Aug 2, 2017

@author: michel
'''
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
