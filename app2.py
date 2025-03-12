import streamlit as st 

st.title("Simple Calculator")

num1 = st.number_input('Enter first number', value= 0.0)
num2 = st.number_input('Enter second number', value= 0.0)

operation = st.selectbox("choose what you want to do with the 2 numbers entered",["+","-","*","/"])

