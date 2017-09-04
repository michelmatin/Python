'''
Created on Jul 26, 2017

@author: michel
'''
name_list = list()
name_dict = dict()
big_name = None
big_count = 0
file_name = input("Enter file:")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
handle = open(file_name, 'r')
# extract the From lines from the mbox-short file
for line in handle:
    if "From " not in line:
        continue
# create a list of each of the words on this line
    words = line.split()
# create and grow the list of the email names by adding the email name of
# this line
    name_list.append(words[1])
#
# Retrieve / Create / Update
# for each name in the name_list, use get function to count the times it
# shows up in name_list, and create a dict called name_dict composed of
# the name:count for each name
for name in name_list:
    name_dict[name] = name_dict.get(name, 0) + 1
# for each name, compare the count value and set big_count to the highest
for key in name_dict:
    if name_dict[key] > big_count:
        big_count = name_dict[key]
        big_name = key
# A tuple method could also be used here instead, where tuple = name_dict.items()
# transforms the dictionary into a list of tuples [(key1,value1), (key2,
# value2), etc]

print(big_name, big_count)
