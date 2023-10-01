# for loop
# Iterate over a sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
   
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# while loop
# Print numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# nested loop
# Multiplication table using nested loops
for i in range(1, 9):
    for j in range(1, 9):
        print(i * j, end=" ")
    print()

#loop control statement
# Break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)
   
# Continue statement
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
   
# Pass statement
for i in range(1, 6):
    if i == 3:
        pass  # the pass statement is a placeholder statement that does nothing
    else:
        print(i)
# When the loop variable i is equal to 3, the pass statement is encountered. The execution simply continues to the next iteration of the loop. For all other values of i, the else block is executed, and the value of i is printed.
