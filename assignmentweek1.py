def simple_calculator():
    """A simple calculator that takes two numbers and an operation."""

    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return # corrected. return is now inside the if block.
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    simple_calculator()

    