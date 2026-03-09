# Python Control Flow & Loop Practice

This repository contains simple Python programs demonstrating the use of control flow statements, loops, and basic data structures.

## Files Included

### Task1.py
Implements **discount rules using if / elif / else**.
- Reads an order amount from the user.
- Applies discounts based on the amount.
- Calculates subtotal, tax (5%), and final amount.
- Handles non-numeric input using exception handling.

### Task2.py
Processes **multiple order amounts using a for loop**.
- Applies discount rules to each order.
- Prints a summary table showing:
  - Order amount
  - Discount
  - Final amount
- Calculates total revenue after discounts.
- Counts how many orders received a discount.

### Task3.py
Implements a **menu-driven program using a while loop**.
- Allows the user to:
  - Add order amounts
  - Display orders with discounts
  - View total revenue
- Uses `break` and `continue` for loop control.

### Task4.py
Demonstrates **loop control using break and continue**.
- Iterates through a list of daily sales.
- `-1` indicates corrupted data and stops processing.
- `0` indicates no sales and skips that day.
- Valid sales are added to a running total.

## Concepts Used

- Python `if / elif / else`
- `for` loops
- `while` loops
- `break` and `continue`
- Lists
- Exception handling
- Basic arithmetic operations

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run any file using:

```bash
python Task1.py