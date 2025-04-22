class Pakuri:
    def __init__(self, name):
        """Initialize a new Pakuri with the given name."""
        self.name = name

    def attack(self, attack_name):
        """Print a message showing the Pakuri using an attack."""
        print(f"{self.name} used {attack_name}!")

    def speak(self):
        """Print a message where the Pakuri speaks."""
        print(f"{self.name}, {self.name}!")

class BankAccount:
    def __init__(self):
        """Initialize a new bank account with a starting balance of 0."""
        self.balance = 0

    def deposit(self, amount):
        """Deposit money if the amount is valid."""
        if amount < 0:
            print("Invalid amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount}")

    def withdraw(self, amount):
        """Withdraw money if the amount is valid and available."""
        if amount < 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("You don't have enough money :(")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}")

    def display(self):
        """Display the current balance."""
        print(f"Current balance: ${self.balance}")

class Coordinate:
    def __init__(self, x, y):
        """Initialize a new coordinate with the given x and y."""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Check if two coordinates are equal."""
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Add two coordinates to create a new coordinate."""
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self):
        """Return a string representation of the coordinate."""
        return f"({self.x}, {self.y})"