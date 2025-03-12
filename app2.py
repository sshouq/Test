import streamlit as st 

st.title("Simple Calculator")

num1 = st.number_input('Enter first number', value= 0.0)
num2 = st.number_input('Enter second number', value= 0.0)

operation = st.selectbox("choose what you want to do with the 2 numbers entered",["+","-","*","/"])

# Calculate button
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = num1 / num2 if num2 != 0 else "Cannot devided by zero"

    st.write(f"Result: {result}")
    

