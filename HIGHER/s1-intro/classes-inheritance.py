# Classes are fundamental to modern programming development. 
# They allow for multiple objects to be created from the same
# template, and therefore access their internal properties.

# More often than not, classes primarily act as collections of
# data that can be read from and written to. However, class based
# inheritance allows for a top-down programming structure to be 
# created in order to allow for multiple data structures that can 
# be used when needed. 

# The clever thing about classes is how they manage data dynamically.
# Previously, you can only define a set of variables that changes 
# globally, or in the scope of functions. Now you can alter the 
# properties of an object basically anywhere! You will see applications
# of this in many instances, and you will see why it is extremely useful.

class Employee:
    def __init__(self, salary: int, name: str, level: int, moneyInAccountCents: int, profession: str) -> None:
        self.salaryCents = salary
        self.name = name
        self.level = level
        self.moneyInAccountCents = moneyInAccountCents
        self.profession = profession
    def pay(self, days: int):
        self.moneyInAccountCents += self.salaryCents * days
        print(f"{self.name} was paid {days} days of salary of {self.salaryCents/100} dollars. Now they have {self.moneyInAccountCents / 100} dollars in their account")
    def buy(self, amountCents: int):
        self.moneyInAccountCents -= amountCents
        print(f"{self.name} bought something that cost him {amountCents/100} dollars. Now they have {self.moneyInAccountCents / 100} dollars in account.")
    def introduce(self):
        print(f"Hi, I am {self.name}. I work as a {self.profession} at level {self.level} with a salary of {self.salaryCents/100} dollars per day. I have {self.moneyInAccountCents / 100} dollars in my bank account.")

john = Employee(10000, "John Doe", "0", 45942, "Programmer")

john.introduce()
john.buy(30000)
john.pay(4)
john.introduce()