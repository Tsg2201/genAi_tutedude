# billing.py
# Contains billing related functions.


# Function to calculate total bill from list of prices
def calculate_total(prices):
    total = sum(prices)
    return total


# Function to apply 5% tax
def apply_tax(amount):
    tax = amount * 0.05
    return amount + tax