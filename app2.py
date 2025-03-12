import streamlit as st 

st.title("Personal Information Form")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 0, 120, 25)
bio = st.text_area("write a short bio")

if st.button("Show my profile"):
    st.markdown(f""" # Profile Information
    **Name:** {name},
    **Age:** {age},
    **Bio:**
    {bio}
    """)
