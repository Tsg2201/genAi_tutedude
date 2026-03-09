"""
Task 5: Safe Shopping Cart
Allows users to enter product prices safely.
Handles invalid inputs and negative prices.
"""

cart = []

while True:

    # Ask user to enter price
    user_input = input("Enter product price (or 'q' to quit): ")

    # Stop program if user enters q
    if user_input.lower() == 'q':
        break

    try:
        # Convert input to float
        price = float(user_input)

        # Raise exception if price is negative
        if price < 0:
            raise ValueError("Price cannot be negative")

        # Add price to cart
        cart.append(price)

    # Handle invalid input
    except ValueError as e:
        print("Invalid input:", e)

# Calculate total bill
total_bill = sum(cart)

print("\nShopping Summary")
print("Total items:", len(cart))
print("Total bill:", total_bill)