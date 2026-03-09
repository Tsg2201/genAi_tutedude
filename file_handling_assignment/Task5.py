# Task 5: Create Product Info File (Exactly 3 Products)

# Open file in write mode
with open("products.txt", "w") as file:

    # Loop exactly 3 times as required
    for i in range(3):

        # Ask user for product details
        name = input("Enter product name: ")
        price = input("Enter product price: ")

        # Write in required format
        file.write(name + " | " + price + "\n")

# Reopen the file and print contents
print("\nProducts stored in file:\n")

with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())