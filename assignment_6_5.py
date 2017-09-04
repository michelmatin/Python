'''
Created on Jul 21, 2017

@author: michel
'''
text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find(":")
startpos = atpos + 4
endpos = startpos + 7
string_num = (text[startpos:endpos])
num = float(string_num)
print(num)
