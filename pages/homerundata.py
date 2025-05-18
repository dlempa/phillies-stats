import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ─── Page Setup ──────────────────────────────────────────────────────────────

st.title("Phillies Fun Stats")
st.subheader("10 Longest Homeruns of the 2025 Season")
st.write("Updated automatically each day after games are completed.")

# ─── Load and Display Data ───────────────────────────────────────────────────

csv_path = "data/homeruns.csv"

if os.path.exists(csv_path):
    # Load data
    df = pd.read_csv(csv_path)

    # Create HTML table
    html = df.to_html(index=False)
    html = html.replace("<th>", "<th align='center'>").replace("<td>", "<td align='center'>")

    # Show styled table
    st.markdown(html, unsafe_allow_html=True)

    # Show last updated timestamp
    updated = datetime.fromtimestamp(os.path.getmtime(csv_path))
    st.caption(f"📅 Last updated: {updated.strftime('%B %d, %Y at %I:%M %p')}")
else:
    st.warning("Data is not available yet. Please check back soon!")
