# Task 4: Loop Control with Conditions (break & continue)

# List of daily sales values
daily = [200, 150, 0, 400, 50, -1, 300]

# Variable to store total sales
total_sales = 0

# Iterate through the list using a for loop
for sale in daily:

    # If value is -1, treat it as corrupted data
    if sale == -1:
        print("Corrupted data encountered. Stopping processing.")
        break  # Stop the loop completely

    # If value is 0, skip it (no sales day)
    if sale == 0:
        print("No sales today. Skipping.")
        continue  # Skip to the next iteration

    # For valid positive sales, add to total
    total_sales += sale

    # Print running total
    print("Added:", sale, "| Running Total:", total_sales)

# Print final total after loop ends
print("\nFinal Total Sales:", total_sales)