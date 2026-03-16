import streamlit as st

price=st.number_input("Enter the price of the Product")
discount=st.slider("Enter the discount percentage",max_value=50,min_value=0,value=0)

final_price=price-(price*discount/100)


if st.button("Calculate"):
    st.write("The final price of the product is",final_price)
    # Optional comparison table
    st.table({"Before":[price], "After":[final_price]})

    