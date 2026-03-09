# discount.py
# Contains functions related to discounts.


# Function to apply percentage discount
def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount


# Function to apply flat discount of 50
def flat_discount(price):
    return price - 50