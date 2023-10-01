name = 'Steven'
age = '16'
text1 = 'My name is {} and I am {} years old'
print(text1.format(name, age))
# The curly bracket is the position where you want to put the variable
# The order of the variable in the text will be the same as it is in the format() method

# Another example
car = 'racing car'
brand = 'BMW'
price = '500k'
text2 = 'This {} from {} costs {}'
print(text2.format(car, brand, price))

# There is the other similar method which can achive the same effect
text3 = f'My name is {name} and I am {age} years old'
print(text3)
# The expected result of text3 should be the same as text1
