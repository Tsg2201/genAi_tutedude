# Task 6: Read File Safely

import os

# Ask user for filename
filename = input("Enter the filename to open: ")

# Check if file exists
if os.path.exists(filename):

    # Open and read file safely
    with open(filename, "r") as file:
        print("\nFile Contents:\n")
        print(file.read())

else:
    print("File not found. Please check the filename.")