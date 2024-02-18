# We use an escape character, when we try to insert characters that are illegal in a string.
# An escape character is a backflash \ followed by the string you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
text = 'My favourite subject is'Math'in school'

# Using escape character to avoid the issue
text1 = 'My facourite subject is \'Math\'in school'
print(text1)
