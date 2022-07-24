import streamlit as st

st.write("""
# Division Calculator
This app will divide a number by another number.
""")
#Get Input
st.header('User Input Parameters')

num = st.number_input("Enter the Dividend")
by  = st.number_input("Enter the Divisor")

st.subheader(f'The result is')
try:
    res = num/by
    st.write(res)
except ZeroDivisionError:
    st.write("Cannot be divided by zero")
