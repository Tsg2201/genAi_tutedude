"""
Task 1: Safe Division Utility
This program divides two numbers entered by the user
and handles possible errors using try-except.
"""

try:
    # Taking numerator input
    numerator = float(input("Enter numerator: "))

    # Taking denominator input
    denominator = float(input("Enter denominator: "))

    # Performing division
    result = numerator / denominator

# Handles invalid number input
except ValueError:
    print("Error: Please enter valid numbers.")

# Handles division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Runs only if no exception occurs
else:
    print("Result:", result)

# Always runs
finally:
    print("Operation Complete")