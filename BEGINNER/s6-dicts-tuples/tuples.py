# Tuples are lists with fixed sizes
# Tuples can be defined with:
# (Note here the use of brackets instead of square brackets to define a tuple)
example_tuple = ("1st element", "2nd element", "3rd element", "4th element", "5th element")

# Accessing individual elements of a tuple
# (Same as accessing elements from a list)
element0 = example_tuple[0]
print(element0) # -> "1st element"
element1 = example_tuple[1]
print(element1) # -> "2nd element"

# Iterating over elements of a tuple
# Using ideas from session 4 -> functions-loops
for element in example_tuple:
    print(element)
    # Guess what this outputs...

# PRACTICE
# The distance between two points on a graph
# (x1, y1) and (x2, y2) 
# is given by distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)

# Given:
p1 = (5, 7)
p2 = (8, 5)
# Calculate and output the distance between p1 and p2
# Write your code here, using variables p1 and p2