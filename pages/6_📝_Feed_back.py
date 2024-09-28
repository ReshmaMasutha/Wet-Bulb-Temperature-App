import streamlit as st
st.title("Feedback")
feedback = st.text_area("Please leave your feedback here:")

if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback!")
    else:
        st.error("Feedback cannot be empty.")
