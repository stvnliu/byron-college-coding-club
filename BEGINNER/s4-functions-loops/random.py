import random

# Generating a random float between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# Generating a random integer within a specified range
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10 (inclusive):", random_integer)

# Generating a random integer within a specified range with a step
random_step_integer = random.randrange(1, 10, 2)
print("Random odd integer between 1 and 10:", random_step_integer)

# Selecting a random element from a list
my_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
random_element = random.choice(my_list)
print("Randomly selected element from the list:", random_element)

# Shuffling a list randomly
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Selecting multiple random elements from a list
random_elements = random.sample(my_list, 2)
print("Two randomly selected elements from the list:", random_elements)

'''
1. random.random(): Generates a random float between 0 and 1.
2. random.randint(a, b): Generates a random integer between a and b (inclusive).
3. random.randrange(start, stop, step): Generates a random integer from start up to, but not including, stop with the specified step.
4. random.choice(sequence): Returns a randomly selected element from the given sequence (e.g., a list).
5. random.shuffle(sequence): Shuffles the elements of a sequence in-place.
6. random.sample(sequence, k): Returns a new list containing k unique elements randomly chosen from the given sequence.
'''
