# Task 7: Mini Project - Export Discounted Prices

# Product price dictionary
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask user for discount percentage
discount = float(input("Enter discount percentage: "))

# Open discount_report.txt to write results
with open("discount_report.txt", "w") as file:

    total_discounted_price = 0

    # Calculate discounted prices
    for product, price in prices.items():

        discounted_price = price - (price * discount / 100)

        total_discounted_price += discounted_price

        # Write formatted output
        file.write(product + " | " + str(price) + " | " + str(round(discounted_price, 2)) + "\n")

    # Write summary
    average_price = total_discounted_price / len(prices)

    file.write("\nTotal Items: " + str(len(prices)) + "\n")
    file.write("Average Discounted Price: " + str(round(average_price, 2)) + "\n")


# Reopen the file and print contents
print("\nDiscount Report:\n")

with open("discount_report.txt", "r") as file:
    print(file.read())