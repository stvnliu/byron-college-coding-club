data = [0, 56, 12, 3556, 6787, 114514, 1919810]

data[0] = 100
print(data)

data[1:3] = [1, 2]
print(data)

data[4:6] = [343]
print(data)
# If you insert less items than you replace,
# the new items will be inserted where you specified, 
# and the remaining items will move accordingly

data[1:2] = [5, 6, 7, 8]
print(data)
# If you insert more items than you replace, 
# the new items will be inserted where you specified,
# and the remaining items will move accordingly

# insert item
data.insert(0, '90')
print(data)
# the position of inserted element is before the index that it is inputted
