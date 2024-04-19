# Submitted by Kosse Dmytro
from random import randint
from tkinter import *
from tkinter import ttk

from random import randint

money_g = 100


def get_bet_amount(money):
  global money_g
  while True:
    if money_g < 0:
      print("You have no money left")
    try:
      bet = int(input(f"How much money out of {money} do you want to bet? "))
      if 0 <= bet <= money:

        return bet
      else:
        print("Invalid bet amount. Please enter a valid amount.")
    except ValueError:
      print("Invalid input. Please enter a valid number.")


def play_game(money):
  global money_g
  number = randint(1, 100)
  #print(f"DEBUG TARGET NUMBER IS {number}")
  bet = get_bet_amount(money)
  guess = int(input("Guess a number between 1-100: "))

  if guess >= number - 5 and guess <= number + 5:
    bet *= 10
    money_g = money_g + bet
    print(f"You won {bet} money. You now have {money_g} money.")
    return True
  else:
    money_g = money_g - bet
    print(f"Sorry, the correct number was {number}.")
    return False


def main(money):
  while money >= 0:
    print(f"You have: {money_g}")
    if play_game(money_g):
      play_again = input("Do you want to play again? [Yes/No] ").lower()
      if play_again != "yes":
        break
    else:
      print("Round over.")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Casino").grid(column=0, row=0)
ttk.Button(frm, text="Play", command=lambda: main(money_g)).grid(column=1,
                                                                 row=0)
root.mainloop()
