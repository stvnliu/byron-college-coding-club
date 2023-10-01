test = 'Hello World'

print(test.upper())
# print test in upper case

print(test.lower())
# print in lower case

print(len(test))
# find the length of the strings
# this works in list too which we will talk about in later sessions

print(test.strip())
# remove space

print(test.replace("d", "ddd"))
# replace d with ddd

print(test.split(' '))
# split the string according to what you entered, the output result won't contain the stirng you entered

print(test.find('Hello'))
# Return the position of the value you entered in the strings

test1 = 'oiiaioiiiai'
print(test1.count('i'))
# return the number of times of the value you entered in the strings

'''
You can check this Python official documentation link for more string methods：  
https://docs.python.org/3/library/stdtypes.html#string-methods
'''
