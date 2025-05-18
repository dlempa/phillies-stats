import streamlit as st

st.set_page_config(page_title="Phillies Stats", page_icon="assets/primary_logo_on_white_color.png", layout="centered")

col1, col2 = st.columns([1, 5])  # adjust width ratio as needed

with col1:
    st.image("assets/primary_logo_on_white_color.png", width=50)

with col2:
    st.title("Phillies Stats Dashboard")

st.markdown("Welcome to the Phillies Stats App! Navigate through the sidebar to explore different statistics.")

st.page_link("pages/Home_Runs.py",label="Home Runs")


st.sidebar.success("Select a page above.")

st.caption(
    "Data is pulled from the unofficial MLB Stats API via the `mlb-statsapi` Python wrapper. "
    "This project is not affiliated with Major League Baseball."
)
