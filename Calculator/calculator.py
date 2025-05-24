import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"
def modulus(x, y): return x % y
def power(x, y): return x ** y
def square_root(x): return math.sqrt(x)

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter your choice (1–8): ").strip()

        try:
            if choice in ['1', '2', '3', '4', '5', '6']:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
            elif choice == '7':
                x = float(input("Enter the number: "))
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
                continue

            if choice == '1':
                result = add(x, y)
                print(f"Addition of {x} and {y} = {result}")
            elif choice == '2':
                result = subtract(x, y)
                print(f"Subtraction of {x} and {y} = {result}")
            elif choice == '3':
                result = multiply(x, y)
                print(f"Multiplication of {x} and {y} = {result}")
            elif choice == '4':
                result = divide(x, y)
                print(f"Division of {x} by {y} = {result}")
            elif choice == '5':
                result = modulus(x, y)
                print(f"Modulus of {x} % {y} = {result}")
            elif choice == '6':
                result = power(x, y)
                print(f"{x} raised to the power of {y} = {result}")
            elif choice == '7':
                result = square_root(x)
                print(f"Square root of {x} = {result}")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

calculator()