from base_classes import *


class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self.password = password

    def get_balance(self, password):
        if password != self.password:
            print("Incorrect password")
            return
        return super().get_balance()

    def deposit(self, amount, password):
        if password != self.password:
            print("Incorrect password")
            return
        super().deposit(amount)

    def withdraw(self, amount, password):
        if password != self.password:
            print("Incorrect password")
            return
        super().withdraw(amount)


class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.previous_result = 0

    def add(self, x, y):
        if x == "RESULT":
            x = self.previous_result
        if y == "RESULT":
            y = self.previous_result
        self.previous_result = super().add(x, y)
        return self.previous_result

    def sub(self, x, y):
        if x == "RESULT":
            x = self.previous_result
        if y == "RESULT":
            y = self.previous_result
        self.previous_result = super().sub(x, y)
        return self.previous_result


class ImprovedFraction(Fraction):
    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return super().add(other)

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return super().multiply(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"
