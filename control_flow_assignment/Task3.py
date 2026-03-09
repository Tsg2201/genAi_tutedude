# Task 3: Menu driven program using while loop

# List to store order amounts
orders = []

# Infinite loop until user quits
while True:

    # Display menu options
    print("\nMenu")
    print("1 - Add order amount")
    print("2 - Show all orders and totals after discount")
    print("q - Quit")

    # Take user choice
    choice = input("Enter your choice: ")

    # Option 1: Add a new order
    if choice == "1":
        amount = float(input("Enter order amount: "))
        orders.append(amount)  # Add order to list

    # Option 2: Show all orders with discounts
    elif choice == "2":

        total = 0

        print("\nOrder -> Discount -> Final Amount")

        # Loop through all stored orders
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

            # Print each order summary
            print(order, "->", discount_amount, "->", final_amount)

            # Add to total
            total += final_amount

        print("Total Amount after Discounts:", total)

    # Option q: Exit program
    elif choice == "q":
        print("Exiting program...")
        break

    # Invalid option
    else:
        print("Invalid choice! Please try again.")
        continue