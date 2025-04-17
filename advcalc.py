# calculator.py - Version 2 (Advanced Calculator using OOP)

import math

class BasicCalculator:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return "Cannot divide by zero!" if y == 0 else x / y

class AdvancedCalculator(BasicCalculator):
    def square(self, x): return x * x
    def square_root(self, x): return "Invalid input!" if x < 0 else math.sqrt
calc = AdvancedCalculator()

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Square Root")
choice = input("Choose operation (1–6): ")

if choice in ['1', '2', '3', '4']:
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if choice == '1': print("Result:", calc.add(a, b))
    elif choice == '2': print("Result:", calc.subtract(a, b))
    elif choice == '3': print("Result:", calc.multiply(a, b))
    elif choice == '4': print("Result:", calc.divide(a, b))

elif choice == '5':
    a = float(input("Enter a number: "))
    print("Square:", calc.square(a))

elif choice == '6':
    a = float(input("Enter a number: "))
    print("Square Root:", calc.square_root(a))

else:
    print("Invalid choice.")
