'''
Created on Jul 27, 2017

@author: michel
'''
# From a mailbox text file, we would like to know what hour every email
# was sent (how many emails were sent for every hour)
hour_dict = dict()
hour_list = list()
file_name = input("Enter file:")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
file_handle = open(file_name, "r")
for line in file_handle:
    # extract only the line of text which have the From, since we are counting
    # the quantity of email from different times
    if not line.startswith("From "):
        continue
# create a list of each word in the line
    words = line.split()
   # print(words)
# the time stamp is the 6th word, it is composed of hours:minutes:seconds
    time = words[5]
    # print(time)
    # Create a list of the [hours,minutes,hours]
    time_digits = time.split(":")
    # print(time_digits)
    # print(time_digits[0])
# extract only the hour, which is the first index position, and add it to
# the list of hour for every email
    hour_list.append(time_digits[0])
# create a dictionary of the hour and a counter for the amount of time it
# is found in the dictionary once added from the hour list
for hour in hour_list:
    hour_dict[hour] = hour_dict.get(hour, 0) + 1
# print(hour_list)
# print(hour_dict)
# create a tuple list from the hour dictionary
tuple_list = hour_dict.items()
# sort the tuple list from smallest k,v to biggest
tuple_list = sorted(tuple_list)

for k, v in tuple_list:
    print(k, v)


# for word in words:
# dic[word] = dic.get(name, 0) + 1
