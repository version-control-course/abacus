# Exercise 1: Viewing and Establishing the Status of a File

class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def add(self):
        pass

    def subtract(self):
        difference = 0
        for item in self.operands:
            difference -= item
        print(difference)

    def divide(self):
        pass

    ddef multiply(self):
        sum  = 1
        for item in self.operands:
            sum *= item
        print(sum)