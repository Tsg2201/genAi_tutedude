products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]

categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics"
]

price_dict = {
    "Laptop": 75000,
    "Smartphone": 40000,
    "Headphones": 3000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

catalog=[(products[i], categories[i], price_dict[products[i]]) for i in range(len(products)  )]
print("Catalog:")
print(catalog)

# Create a mapping of category to products
category_to_products={category: [product for product, cat, price in catalog if cat == category] for category in set(categories)}
print("Category to products mapping:")
print(category_to_products)

#Find category with maximum products
max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("Category with most products:", max_category)

print("Products in that category:")
for p in category_to_products[max_category]:
    print(p)