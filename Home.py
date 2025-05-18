import streamlit as st

st.set_page_config(page_title="Phillies Stats", page_icon="assets/primary_logo_on_white_color.png", layout="centered")
st.image("assets/primary_logo_on_white_color.png", width=50)
st.title("⚾ Phillies Stats Dashboard")
st.markdown("Welcome to the Phillies Stats App! Navigate through the sidebar to explore different statistics.")




st.sidebar.success("Select a page above.")

st.caption(
    "Data is pulled from the unofficial MLB Stats API via the `mlb-statsapi` Python wrapper. "
    "This project is not affiliated with Major League Baseball."
)
