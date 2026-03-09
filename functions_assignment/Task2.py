# ==============================
# Task 2 – Recursive Function
# Factorial Utility
# ==============================

def factorial(n):
    """
    Returns factorial of n using recursion.
    Handles edge cases: n = 0, n = 1
    Prints error message if n is negative
    """

    # Handle negative numbers
    if n < 0:
        print("Error: Factorial not defined for negative numbers")
        return

    # Base cases
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Test cases
print("Testing Task 2")

print("factorial(5):", factorial(5))
print("factorial(0):", factorial(0))
print("factorial(-3):", factorial(-3))