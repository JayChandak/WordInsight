import streamlit as st
from core.word_generator import get_category_words
from ui import render_ui

st.set_page_config(page_title="Category Word Explorer", layout="centered")

# --- Hide Top Right Menu & Toolbar ---
hide_top_right = """
    <style>
    .stActionButton, .stToolbar {visibility: hidden;}
    [data-testid="stToolbarActions"] {display: none;}
    [data-testid="stActionButtonIcon"] {display: none;}
    </style>
"""
st.markdown(hide_top_right, unsafe_allow_html=True)

st.title("Category Word Explorer")

# --- Session State ---
if "words_data" not in st.session_state:
    st.session_state.words_data = []
if "current_category" not in st.session_state:
    st.session_state.current_category = ""

# --- Input ---
category = st.text_input("Enter a category (e.g., Finance, Technology, Science):", 
                         st.session_state.current_category)

# --- Generate Words Button ---
if st.button("Generate Words"):
    if category.strip():
        st.session_state.current_category = category
        with st.spinner("Fetching words..."):
            st.session_state.words_data = get_category_words(category)
    else:
        st.warning("Please enter a category first.")

# --- Refresh Button ---
if st.session_state.words_data:
    if st.button("🔄 Refresh Words"):
        with st.spinner("Fetching new words..."):
            st.session_state.words_data = get_category_words(st.session_state.current_category)

# --- Display Words ---
if st.session_state.words_data:
    render_ui(st.session_state.words_data)
