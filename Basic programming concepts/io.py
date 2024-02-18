# This is output
print("I am the output result, uwu")

# This is an input. An input will ALWAYS be a str type. 
# To convert it to another type, enclose it in int(), float(), str(), or other methods.
number = input("Write here any number you like: ")

print(number)

# The following 2 print statements concatenate a string with another string 
print("The number is "+ number)
print("The number is ", number)

# f-strings are basically "syntactic sugar" to make the code for concatenating strings 
# look nicer by inserting the variable in the code directly.
# Example
x = 128324 # pretend this is some kind of result from a process
print(f"The result of the calculation is {x}")

