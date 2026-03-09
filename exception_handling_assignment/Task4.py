"""
Task 4: File Reader with Exception Handling
Reads the first 3 lines of a file.
Handles file-related errors.
"""

# Ask user for filename
filename = input("Enter filename: ")

try:
    # Attempt to open file
    file = open(filename, "r")

    print("First 3 lines of the file:")

    # Print first 3 lines
    for i in range(3):
        line = file.readline()
        print(line.strip())

    file.close()

# File not found error
except FileNotFoundError:
    print("Error: File not found.")

# Permission issue
except PermissionError:
    print("Error: Permission denied.")

# Always execute
finally:
    print("File operation attempted.")