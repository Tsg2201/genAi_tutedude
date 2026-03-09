"""
Task 3: Custom Exception - Age Validator
Checks whether the user's age is between 1 and 120.
"""

# Function to validate age
def check_age(age):

    # Raise custom exception if age is invalid
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")


try:
    # Take age input from user
    age = int(input("Enter your age: "))

    # Call validation function
    check_age(age)

    print("Age is valid.")

# Catch and display custom error
except ValueError as e:
    print("Error:", e)