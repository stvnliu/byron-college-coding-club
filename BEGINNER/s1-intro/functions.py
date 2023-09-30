# Functions are objects that take a number of inputs and spit out an output
def do_something(arg1: str, arg2: str):
    print(f"I am doing something with {arg1} and {arg2}...")
    result = arg1.capitalize()[2:-1]
    result = result + arg2[0]
    print("I have finished. Now I will return the result of my doing something")
    return result # Returns a value to be used by another process

# Functions allow us to reuse code that has been written once already to 
# avoid repeating yourself. Why? Because programmers are lazy and don't 
# want to write things twice.

print(do_something("Apple", "Banana"))
print(do_something("China", "America"))

# Discussion
# It is usually 