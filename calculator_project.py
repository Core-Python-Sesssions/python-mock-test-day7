"""
Mini Project: Build a Menu-Based Calculator

Features:
- Addition
- Subtraction
- Multiplication
- Division

Enhancements (optional):
- Power, Modulo, Square Root
- Input validation
"""

def calculator():
    print("Welcome to Calculator!")
    print("Select operation:")
    print("1. Add
2. Subtract
3. Multiply
4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
