class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."


calculator = Calculator()
num1=int(input("ENTER FIRST NUMBER: "))
num2=int(input("ENTER SECOND NUMBER: "))
print(f"Addition: {num1} + {num2} = {calculator.add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {calculator.subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {calculator.multiply(num1, num2)}")
print(f"Division: {num1} / {num2} = {calculator.divide(num1, num2)}")


