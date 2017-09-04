'''
Created on Jul 21, 2017

@author: michel
'''
largest = None
smallest = None
while True:
    numstr = input("Enter a number: ")
    if numstr == "done":
        break
    try:
        num = int(numstr)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
    if smallest is None:
        smallest = num

    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num


print("Maximum is", largest)
print("Minimum is", smallest)
