# 1. Create a dictionary with at least 6 entries
price_dict = {
    "Laptop": 75000,
    "Smartphone": 40000,
    "Headphones": 3000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

print("Initial price dictionary:", price_dict)


# 2A. Add a new product
price_dict["Tablet"] = 25000
print("After adding Tablet:", price_dict)


# 2B. Update the price of an existing product
price_dict["Laptop"] = 72000
print("After updating Laptop price:", price_dict)


# 2C. Remove a product safely
product_to_remove = "Mouse"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"{product_to_remove} removed.")
else:
    print("Product not found.")

print("Updated price dictionary:", price_dict)


# 3. Print the average price
total = sum(price_dict.values())
count = len(price_dict)

average_price = total / count
print("Average price:", average_price)


# Extra: Find product with max and min price
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive product:", max_product, price_dict[max_product])
print("Cheapest product:", min_product, price_dict[min_product])