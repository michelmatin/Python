'''
Created on Jul 31, 2017

@author: michel
'''
import re
sum = 0
file_name = input("Enter the filename: ")
file_handle = open(file_name, "r")
for line in file_handle:
    num = re.findall("([0-9]+)", line)
    if len(num) < 1:
        continue
 #   print(num)
    for number in num:
        sum = sum + int(number)
print("Sum: ", sum)
