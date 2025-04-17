# calculator.py - Version 1 (Normal Calculator with Loop)

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Cannot divide by zero!" if y == 0 else x / y

while True:
    print("\nSimple Calculator")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
