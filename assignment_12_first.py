'''
Created on Aug 2, 2017

@author: michel
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")
# print(soup)
span_results = soup.find_all('span')
# print(span_results)
for span in span_results:
    # print(span)
    object_list = str(span)
    num = re.findall('<span class="comments">([0-9]+)</span>', object_list)
    if len(num) > 0:
        # print(num)
        # print(int(num[0]))
        sum = sum + int(num[0])
print("Sum", sum)
