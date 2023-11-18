import random

def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

def guess_number(target, guess):
    if guess < target:
        return "Too low! Try again."
    elif guess > target:
        return "Too high! Try again."
    else:
        return f"Congratulations! You guessed the correct number ({target})."

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Set the range for the random number
    minimum = 1
    maximum = 100
    target_number = generate_random_number(minimum, maximum)

    while True:
        user_guess = int(input(f"Guess a number between {minimum} and {maximum}: "))
        feedback = guess_number(target_number, user_guess)
        print(feedback)

        if user_guess == target_number:
            break

# Run the game
number_guessing_game()
