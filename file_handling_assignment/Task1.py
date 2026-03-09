# Task 1: Write Sales Records to a File

# Step 1: Create a list of sales amounts
sales = [1200, 450, 980, 1500, 3000]

# Step 2: Open the file in write mode ('w')
# 'with' ensures the file closes automatically
with open("sales_data.txt", "w") as file:
    
    # Step 3: Write each sale on a new line
    for amount in sales:
        file.write(str(amount) + "\n")

# Step 4: Reopen the file and print its contents
with open("sales_data.txt", "r") as file:
    print("Contents of sales_data.txt:")
    print(file.read())