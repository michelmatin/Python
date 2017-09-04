'''
Created on Jul 25, 2017

@author: michel
'''
# Use the file name mbox-short.txt as the file name
num = 0
spam = 0
average_spam = 0
counter = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    atpos = line.find(":")
    startpos = atpos + 2
    endpos = startpos + 7
    string_num = (line[startpos:endpos])
    num = float(string_num)
    counter = counter + 1
    spam = spam + num
average_spam = spam / counter
print("Average spam confidence:", average_spam)
