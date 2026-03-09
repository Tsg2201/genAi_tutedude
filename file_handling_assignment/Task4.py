# Task 4: Generate Summary Report from File

# Open the sales_data.txt file and read values
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# Convert lines to integers after removing newline characters
sales = [int(line.strip()) for line in lines]

# Calculate required statistics
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# Print results
print("Sales Summary Report")
print("--------------------")
print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)