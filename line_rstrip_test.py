'''
Created on Jul 27, 2017

@author: michel
'''
filename = input("Enter Filename: ")
file_handle = open(filename, "r")
for line in file_handle:
    line = line.rstrip()
    print(line)
