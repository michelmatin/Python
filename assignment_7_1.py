'''
Created on Jul 24, 2017

@author: michel
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line_no_newline = line.rstrip()
    print(line_no_newline.upper())
