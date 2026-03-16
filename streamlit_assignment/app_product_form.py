import streamlit as st

st.title("Product Form")

# Sidebar inputs
name = st.sidebar.text_input("Enter Product Name")

category = st.sidebar.selectbox(
    "Select Category",
    ["Electronics", "Clothing", "Food", "Books", "Other"]
)

price = st.sidebar.number_input("Enter Price", min_value=0.0)

# Button
add_product = st.sidebar.button("Add Product")

# When button is clicked
if add_product:
    st.success("Product added successfully!")

    st.subheader("Product Details")

    st.write(f"Product Name: {name}")
    st.write(f"Category: {category}")
    st.write(f"Price: ₹{price}")