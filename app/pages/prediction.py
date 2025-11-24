import streamlit as st


st.set_page_config(page_title="Spam Detector", page_icon=":tada:", layout="wide")

st.title("Spam Detector")
st.subheader("Detect spam emails with ease")
st.write("This app uses machine learning to detect spam emails.")

st.write("Enter an email below to detect if it is spam or not.")

email = st.text_input("Email")

if st.button("Detect"):
    st.write("This email is spam.")
    