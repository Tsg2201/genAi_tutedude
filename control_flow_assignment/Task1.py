# Task 1: Discount Rules using if / elif / else

try:
    # Take input from user and convert it to float
    order_amount = float(input("Enter order amount: "))

    # Determine discount percentage based on order amount
    if order_amount >= 2000:
        discount_rate = 0.15
    elif order_amount >= 1500:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0

    # Calculate discount amount
    discount_amount = order_amount * discount_rate

    # Calculate subtotal after discount
    subtotal = order_amount - discount_amount

    # Apply fixed tax of 5%
    tax = subtotal * 0.05

    # Calculate final total
    final_total = subtotal + tax

    # Print results
    print("\nOrder Amount:", order_amount)
    print("Discount Applied:", discount_amount)
    print("Subtotal after Discount:", subtotal)
    print("Tax (5%):", tax)
    print("Final Amount to Pay:", final_total)

# Handle case where input is not a number
except ValueError:
    print("Invalid input! Please enter a numeric value.")