import streamlit as st
import os
import sys


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sys.path.append(BASE_DIR)

from db.database import init_db

init_db()

st.set_page_config(page_title="Doc_Manager", layout="wide")

st.title("Smart PDF Document Manager")

st.divider()

tabs = st.tabs(["Upload", "Search and View", "Analytics"])

with tabs[0]:
    pass

with tabs[1]:
    pass

with tabs[2]:
    pass