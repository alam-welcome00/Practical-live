import streamlit as st
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sys.path.append(BASE_DIR)

from db.database import init_db
from core.servicies import DocumentService


init_db()
service = DocumentService()
st.set_page_config(page_title="Doc_Manager", layout="wide")

st.title("Smart PDF Document Manager")

st.divider()

tabs = st.tabs(["Upload", "Search and View", "Analytics"])

with tabs[0]:
    st.header("Upload PDF")
    pdf = st.file_uploader("Upload PDF",type="pdf")
    tags = st.text_input("Tags (Comma seperated)")
    description = st.text_area("Description")
    lecture_Date = st.date_input("Lecture Date",value=None)

    if st.button("Upload"):
        if pdf:
            service.upload_doc(pdf, tags, description, lecture_Date)
        else:
            st.error("Please upload pdf file")

with tabs[1]:
    pass

with tabs[2]:
    pass