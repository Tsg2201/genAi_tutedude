# ==============================
# Task 1 – Basic Function
# Price After Discount
# ==============================

def apply_discount(price, discount_percent=5):
    """
    Returns the price after applying discount.
    Default discount is 5% if not provided.
    Discount cannot exceed 60%.
    """

    # Ensure discount does not exceed 60%
    if discount_percent > 60:
        discount_percent = 60

    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount

    return final_price


# Test cases
print("Testing Task 1")

print(apply_discount(1000, 10))   # Expected: 900
print(apply_discount(500))        # Uses default 5% discount