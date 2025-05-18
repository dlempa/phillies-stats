import streamlit as st
import pandas as pd

st.title("Phillies Fun Stats")
st.subheader("10 Longest Homeruns of the 2025 Season")
st.write("Updated automatically each day after games are completed")

try:
    df = pd.read_csv("data/homeruns.csv")
    st.dataframe(df)
except FileNotFoundError:
    st.error("No homerun data available yet. Please check back later.")
