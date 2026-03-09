# main.py
# This file tests all modules and package functions.


# -------- Import math_utils in two ways --------
import math_utils
from math_utils import square


# -------- Import string_utils --------
import string_utils


# -------- Import package modules --------
import shop_package.discount as disc
from shop_package.billing import calculate_total


# ---------- Testing math_utils ----------
print("MATH FUNCTIONS")
print("Add:", math_utils.add(10, 5))
print("Subtract:", math_utils.subtract(10, 5))
print("Square:", square(4))


# ---------- Testing string_utils ----------
print("\nSTRING FUNCTIONS")

text = "hello world from python"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# ---------- Testing shop_package ----------
print("\nSHOP PACKAGE FUNCTIONS")

# Discount functions
print("Apply Discount:", disc.apply_discount(1000, 10))
print("Flat Discount:", disc.flat_discount(1000))

# Billing functions
prices = [100, 200, 300]

print("Total Bill:", calculate_total(prices))