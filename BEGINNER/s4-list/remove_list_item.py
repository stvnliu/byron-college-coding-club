fruits = ["Apple", "Banana", "Peach"]
fruits1 = fruits

fruits.remove("Peach")
print(fruits)
# This remove a specific element that you want

fruits.pop(0)
print(fruits)
# This will delete the element with coresponding index

del fruits1[0]
# This will delete the element with coresponding index too

del fruits1
# This will delete the whole list
