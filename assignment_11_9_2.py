'''
Created on Jul 29, 2017

@author: michel
'''
import re
num_list = list()
total_num = 0
av_counter = 0
file_name = input("Enter the filename: ")
file_handle = open(file_name, "r")
for line in file_handle:
    line = line.rstrip()
    if not re.search("New Revision: [0-9.]+", line):
        continue
    else:
        line_number = re.findall("New Revision: [0-9.]+", line)
        number_list = re.findall("New Revision: ([0-9.]+)", line)
        number = float(number_list[0])
        print(line_number)
        print(number)
        num_list.append(number)
print(num_list)
for num in num_list:
    total_num = total_num + num
    av_counter = av_counter + 1
average = total_num / av_counter
print("Average: ", round(average, 7))
