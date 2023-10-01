# You will come to scenarios where you want to handle an Exception 
# to modify how your program works under known scenarios

# In these scenarios, use the try-except syntax
try:
    raw_input = input("Input literally anything: ")

    # Converts the input into an integer type
    # Throws ValueError if the input is not a number
    number = int(raw_input)
    print("Your program didn't produce an exception. You deserve a lolipop!")
    print(f"Your input was {number}, what would happen if you put something that wasn't a number?")
except ValueError as error:
    print(error)
    print("ValueError has occured. What you entered is not a number :(")

# Discussion
# The program branches into 2 paths, one that is the normal execution logic, 
# another with an exception occuring. This is usually seen in file handling,
# where the file handler may produce an exception when the file is not found.
# This doesn't mean the code has a bug, instead it means the program needs 
# an alternative method to consider when the file has not been created yet.
# Perhaps you will need to create a new file, or overwrite an existing one.
# 
# It is important to remember that Exceptions != Bugs. It is commonplace for
# Standard libraries to use exceptions as branches for certain conditions, or
# to filter out unreasonable values. More often than not, you use exception 
# handling to