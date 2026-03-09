# Task 3: Append New Sales

# New sales values to add
new_sales = [5000, 2500, 1700]

# Open file in append mode ('a')
with open("sales_data.txt", "a") as file:
    
    # Add each new sale on a new line
    for amount in new_sales:
        file.write(str(amount) + "\n")

# Reopen the file to print updated contents
with open("sales_data.txt", "r") as file:
    updated_data = file.readlines()

print("Updated file contents:")
for line in updated_data:
    print(line.strip())

# Extra: Print total number of lines
print("Total number of sales records:", len(updated_data))