'''
Created on Jul 26, 2017

@author: michel
'''
file_name = input("Enter file name: ")
file_handle = open(file_name, 'r')
lst = list()
for line in file_handle:
    line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
