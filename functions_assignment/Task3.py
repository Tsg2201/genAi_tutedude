# ==============================
# Task 3 – Lambda Function
# GST Calculator
# ==============================

# Lambda to add 18% GST
gst = lambda price: price + (0.18 * price)

print("GST on 100:", gst(100))


# Optional: GST + Discount together
gst_discount = lambda price, discount: (price + 0.18 * price) - ((price + 0.18 * price) * discount / 100)

print("Price after GST + 10% discount:", gst_discount(100, 10))