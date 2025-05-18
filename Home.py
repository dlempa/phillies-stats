import streamlit as st

st.set_page_config(page_title="Phillies Stats", page_icon="⚾", layout="centered")

st.title("⚾ Phillies Stats Dashboard")
st.markdown("Welcome to the Phillies Stats App! Navigate through the sidebar to explore different statistics.")

st.image("https://upload.wikimedia.org/wikipedia/en/6/6d/Philadelphia_Phillies_logo.png", width=200)


st.sidebar.success("Select a page above.")

with st.expander("⚠️ Data Disclaimer"):
    st.markdown(
        """
        This app uses data obtained via the [unofficial MLB Stats API](https://statsapi.mlb.com/api/), 
        accessed using the open-source [`mlb-statsapi`](https://github.com/toddrob99/MLB-StatsAPI) Python wrapper.

        This project is not affiliated with or endorsed by Major League Baseball or its partners.
        All data is intended for educational and non-commercial purposes.
        """
    )
