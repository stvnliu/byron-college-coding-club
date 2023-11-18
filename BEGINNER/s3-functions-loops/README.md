# Exercise: Number Guessing

## Problem Statement:  

You are tasked with creating a number guessing game. The program should generate a random number between a specified range and ask the user to guess the number. The program should provide feedback on whether the user's guess is too high, too low, or correct. The game should continue until the user correctly guesses the number.  

**YOU WILL NEED TO USE A LIBRARY CALLED [random](https://docs.python.org/3/library/random.html).**

## Requirements:
1. Create a function generate_random_number(minimum, maximum) that generates and returns a random number within the specified range [minimum, maximum].
  
2. Create a function guess_number(target, guess) that takes the target number and the user's guess as parameters and provides feedback on whether the guess is too high, too low, or correct.  
   
3. Use a loop to repeatedly prompt the user for their guess until they guess the correct number.
  
4. Provide appropriate messages to guide the user during the guessing process.

## Expected Output:
```
Welcome to the Number Guessing Game!

Guess a number between 1 and 100: 50
Too low! Try again.

Guess a number between 1 and 100: 75
Too high! Try again.

Guess a number between 1 and 100: 60
Too low! Try again.

Guess a number between 1 and 100: 70
Too high! Try again.

Guess a number between 1 and 100: 65
Congratulations! You guessed the correct number (65).
```
