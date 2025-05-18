import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ─── Page Setup ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Home Run Stats", page_icon="🏠")
st.title("Home Run Stats")
st.write("Updated automatically each day after games are completed.")





# ─── Load and Display Data for Longest Homeruns of 2025 Season ───────────────────────────────────────────────────
st.subheader("10 Longest Homeruns of the 2025 Season")
csv_path = "data/homeruns.csv"

if os.path.exists(csv_path):
    # Load data
    df = pd.read_csv(csv_path)

    # Create HTML table
    html = df.to_html(index=False)
    html = html.replace("<th>", "<th align='center'>").replace("<td>", "<td align='center'>")

    # Show styled table
    st.markdown(html, unsafe_allow_html=True)
