# # app.py
# import streamlit as st
# from core.word_generator import get_category_words
# from ui import render_ui

# st.title("Category Word Explorer")

# category = st.text_input("Enter a category (e.g., Finance, Technology, Science):")

# if st.button("Generate Words"):
#     if category.strip():
#         with st.spinner("Fetching words..."):
#             words_data = get_category_words(category)
#         render_ui(words_data)
#     else:
#         st.warning("Please enter a category first.")

import streamlit as st
from core.word_generator import get_category_words
from ui import render_ui

st.title("Category Word Explorer")

# --- Session State ---
if "words_data" not in st.session_state:
    st.session_state.words_data = []
if "current_category" not in st.session_state:
    st.session_state.current_category = ""

# --- Input ---
category = st.text_input("Enter a category (e.g., Finance, Technology, Science):", 
                         st.session_state.current_category)

# --- Generate Button ---
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

# --- Display UI ---
if st.session_state.words_data:
    render_ui(st.session_state.words_data)
