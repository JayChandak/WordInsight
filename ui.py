# ui.py
import streamlit as st

def render_ui(words_data: list[dict]):
    # st.subheader("Top 10 Words")
    for item in words_data:
        st.markdown(f"**{item['word']}**: {item['definition']}")
