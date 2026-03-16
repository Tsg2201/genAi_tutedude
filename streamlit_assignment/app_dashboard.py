import streamlit as st

st.title("Simple sales Dashboard")
st.write("This is a simple sales dashboard")

months = ["January" , "February", "March", "April"]
sales={"January":1200,"February":1500,"March":900,"April":2000}

selectedMonth=st.selectbox("Select a month",months)

if selectedMonth:
    st.write("Sales for",selectedMonth,":",sales[selectedMonth])

st.bar_chart(sales)