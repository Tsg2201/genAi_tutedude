# Task 2: Apply discounts to multiple orders using a for loop

# List of order amounts
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0          # Stores total revenue after discounts
discounted_orders = 0      # Counts orders that received a discount

print("Order -> Discount -> Final Amount")

# Loop through each order
for order in orders:

    # Determine discount rate
    if order >= 2000:
        discount_rate = 0.15
    elif order >= 1500:
        discount_rate = 0.10
    elif order >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0

    # Calculate discount and final price
    discount_amount = order * discount_rate
    final_amount = order - discount_amount

    # Print summary row
    print(order, "->", discount_amount, "->", final_amount)

    # Add to total revenue
    total_revenue += final_amount

    # Count orders that got a discount
    if discount_rate > 0:
        discounted_orders += 1

# Print totals
print("\nTotal Revenue after Discounts:", total_revenue)
print("Number of Orders with Discount:", discounted_orders)