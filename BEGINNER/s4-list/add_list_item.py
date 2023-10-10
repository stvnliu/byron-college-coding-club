list1 = [1, 2, 3]
list2 = [4, 5, 6]

# add item to the end of the list
list1.append(4)
print(list1)

# extend the list
list1.extend(list2)
print(list1)
# two lists are going to be combined together
# you can extend thw list with tuple, sets, dictionaries etc. too
# Eg:
tuple = ("hello", "world")
newlist = [1, 2, 3, 4]
newlist.extend(tuple)
