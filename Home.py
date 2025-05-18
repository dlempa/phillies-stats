import streamlit as st

st.set_page_config(page_title="Phillies Stats", page_icon="⚾", layout="centered")

st.title("⚾ Phillies Stats Dashboard")
st.markdown("Welcome to the Phillies Stats App! Navigate through the sidebar to explore different statistics.")

st.image("https://upload.wikimedia.org/wikipedia/en/6/6d/Philadelphia_Phillies_logo.png", width=200)

st.markdown("### 📊 Available Pages")
st.markdown("- [Home Run Data](./homerundata)")

st.sidebar.success("Select a page above.")
