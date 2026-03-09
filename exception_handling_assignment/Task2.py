"""
Task 2: Bill Calculator with Error Handling
This program processes a list of product prices
and calculates the running total while handling errors.
"""

prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:
    try:
        # Check if the value is numeric
        if not isinstance(price, (int, float)):
            raise TypeError("Invalid price type")

        # Raise custom error for negative price
        if price < 0:
            raise ValueError("Negative price not allowed")

        # Add valid price to total
        total += price

    # Handle non-numeric values
    except TypeError:
        print("Skipping invalid item:", price)

    # Handle negative price
    except ValueError as e:
        print("Error:", e)

    # Print running total after each step
    finally:
        print("Running total:", total)