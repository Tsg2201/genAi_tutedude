# Parallel list of categories for each product
categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics"
]

# 1. Create a set of categories from the list
categories_set = set(categories)
print("Unique categories:", categories_set)

# 2. Add a new category and show duplicates are ignored
categories_set.add("Accessories")   # already exists
categories_set.add("Wearables")     # new category
print("After adding categories:", categories_set)

# 3. Check if a category exists in the set
check_category = "Electronics"
print("Does 'Electronics' exist?", check_category in categories_set)

# Extra: Get total number of unique categories
print("Total unique categories:", len(categories_set))