# 1. Create a list named products containing at least 6 product names
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]

# 2. Create a tuple named sample_product (product_name, price, category)
sample_product = ("Laptop", 75000, "Electronics")

# 3. Print the 2nd and last product from the products list
print("2nd product:", products[1])
print("Last product:", products[-1])

# 4. Append two new product names and print the updated list
products.append("Tablet")
products.append("Smartwatch")

print("Updated products list:", products)

# Extra (optional):
# Convert sample_product to a list, change its price, then convert it back to a tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 70000   # change price

sample_product = tuple(sample_product_list)

print("Updated sample product tuple:", sample_product)