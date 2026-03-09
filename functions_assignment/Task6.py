# ==============================
# Task 6 – Combined Utility
# ==============================

def process_prices(prices):

    # Apply 10% discount
    discounted_prices = list(map(lambda price: price - (0.10 * price), prices))

    # Keep only prices above 300
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))

    return discounted_prices, filtered_prices


# Test
discounted, filtered = process_prices([100, 500, 900, 50, 750])

print("Discounted prices:", discounted)
print("Filtered prices (>300):", filtered)