'''
Created on Jul 29, 2017

@author: michel
'''
import re
line_counter = 0
file_name = input("Please enter the filename: ")
if len(file_name) < 1:
    file_name = "mbox.txt"
file_handle = open(file_name, "r")
expression = input("Enter a regular expression: ")

for line in file_handle:
    if not re.search(expression, line):
        continue
    else:
        print(line)
        line_counter = line_counter + 1
print(file_name, "had", line_counter, "lines that matched", expression)
