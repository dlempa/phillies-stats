import streamlit as st
import pandas as pd
import os
from datetime import datetime
from zoneinfo import ZoneInfo  # Optional, for EST
import altair as alt

# ─── Page Setup ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Home Run Stats", page_icon="🏠")
st.title("Home Run Stats")
st.write("Updated automatically each day after games are completed.")

# ─── File Paths ──────────────────────────────────────────────────────────────
csv_top10 = "data/homeruns_top10.csv"
csv_all = "data/homeruns_all.csv"

# ─── Load and Display Data ───────────────────────────────────────────────────
if os.path.exists(csv_top10) and os.path.exists(csv_all):
    df_top10 = pd.read_csv(csv_top10)
    df_all = pd.read_csv(csv_all)

    # ─── Styled Table ────────────────────────────────────────────────────────
    st.subheader("🔝 10 Longest Homeruns of the 2025 Season")

    html = df_top10.to_html(index=False)
    html = html.replace("<th>", "<th align='center'>").replace("<td>", "<td align='center'>")
    st.markdown(html, unsafe_allow_html=True)

    # ─── Last Updated Timestamp ─────────────────────────────────────────────
    updated = datetime.fromtimestamp(os.path.getmtime(csv_top10), ZoneInfo("America/New_York"))
    st.caption(f"📅 Last updated: {updated.strftime('%B %d, %Y at %I:%M %p EST')}")

    st.divider()
    # ─── Timeline Chart ─────────────────────────────────────────────────────
    st.subheader("📈 Homerun Visualization")

    df_all["Date"] = pd.to_datetime(df_all["Date"])
    chart = alt.Chart(df_all).mark_circle(size=100).encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("Distance:Q", title="Distance (feet)"),
        color=alt.Color("Hitter:N", title="Player"),
        tooltip=["Hitter", "Distance", "Opponent", "Ballpark", "Date"]
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

else:
    st.warning("⚠️ Homerun data is not available yet. Please check back soon!")
