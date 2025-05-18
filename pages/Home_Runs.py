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
csv_top10 = "data/homeruns_top10.csv"

if os.path.exists(csv_path):
    # Load data
    df = pd.read_csv(csv_path)

    # Create HTML table
    html = df.to_html(index=False)
    html = html.replace("<th>", "<th align='center'>").replace("<td>", "<td align='center'>")

    # Show styled table
    st.markdown(html, unsafe_allow_html=True)

# ─── Load and Display Data for Longest Homeruns of 2025 Season ───────────────────────────────────────────────────
st.subheader("Homerun Visualization")
csv_all = "data/homeruns_all.csv"

# Timeline Chart
df_all["Date"] = pd.to_datetime(df_all["Date"])
chart = alt.Chart(df_all).mark_circle(size=100).encode(
    x=alt.X("Date:T", title="Date"),
    y=alt.Y("Distance:Q", title="Distance (feet)"),
    color=alt.Color("Hitter:N", title="Player"),
    tooltip=["Hitter", "Distance", "Opponent", "Ballpark", "Date"]
).interactive()
