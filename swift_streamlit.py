import numpy as np
import pandas as pd
import streamlit as st
from introduction import introduction
from album_overview import album_overview

st.set_page_config(page_title="The Swift Data Expedition", layout="wide", page_icon="&#127908")
st.markdown("<h1 style='text-align: center;'>&#127908</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>The Swift Data Expedition</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>An Analysis of Taylor Swift Music</h2>", unsafe_allow_html=True)

#Define a dictionary with the page names and their respective functions
pages = {
    "📝 Introduction": introduction,
    "Overview": album_overview
}

st.sidebar.title("Table of Contents")

# Create a radio button in the sidebar to select a page
page = st.sidebar.radio("", list(pages.keys()))

# Display the selected page with the corresponding function
pages[page](display=True)