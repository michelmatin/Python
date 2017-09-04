'''
Created on Jul 26, 2017

@author: michel
'''
count = 0
filename = input("Enter the file name: ")
file_handle = open(filename, "r")
for line in file_handle:
    if "From " not in line:
        continue
    count = count + 1
    words = line.split()
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
