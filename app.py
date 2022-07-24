import streamlit as st

st.write("""
# Division Calculator
This app will divide a number by another number.
""")
#Get Input
st.header('User Input Parameters')

num = st.number_input("Enter the Dividend")
by  = st.number_input("Enter the Divisor")

st.write(f'The result of {num}/{by} = {num/by}')
