# Task 2: Read File in Different Ways

# Open the existing sales_data.txt file
with open("sales_data.txt", "r") as file:
    
    # 1. Read the entire file
    print("Reading entire file using read():")
    content = file.read()
    print(content)

# Reopen the file to reset the cursor
with open("sales_data.txt", "r") as file:
    
    # 2. Read the first line
    first_line = file.readline()
    print("First line using readline():", first_line.strip())

# Reopen again to read all lines
with open("sales_data.txt", "r") as file:
    
    # 3. Read all lines using readlines()
    lines = file.readlines()
    
    # Convert lines to integers and remove newline characters
    sales_numbers = [int(line.strip()) for line in lines]

    print("Sales numbers list:", sales_numbers)