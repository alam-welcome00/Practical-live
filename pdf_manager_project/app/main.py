import streamlit as st
import os
import sys
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sys.path.append(BASE_DIR)

load_dotenv(os.path.join(BASE_DIR,".env"))
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

from db.database import init_db
from core.servicies import DocumentService
from core.reader import ReadPdf
from core.analytics import Analytics_service

if "search_results" not in st.session_state:
    st.session_state.search_results = []

if "reader_mode" not in st.session_state:
    st.session_state.reader_mode = False

if "selected_doc" not in st.session_state:
    st.session_state.selected_doc = None

if "current_page" not in st.session_state:
    st.session_state.current_page = 0

if "show_reset" not in st.session_state:
    st.session_state.show_reset = False
init_db()
service = DocumentService()
st.set_page_config(page_title="Doc_Manager", layout="wide")
analytics_service=Analytics_service()

st.title("Smart PDF Document Manager")

st.divider()

st.subheader("Admin Control")

if st.button("Clean DataBase"):
    st.session_state.show_reset = True

if st.session_state.show_reset:
    password_input= st.text_input("Enter Admin Password",type="password")

    if st.button("Confirm Reset"):
        if password_input == ADMIN_PASSWORD:
            st.write("Loaded Password:", ADMIN_PASSWORD)
            import shutil

            if os.path.exists("data/documents.db"):
                os.remove("data/documents.db")

            pdf_dir = os.path.join("storage","pdf")
            thumbnail_dir = os.path.join("storage","thumbnails")
            img_dir = os.path.join("storage","pdfs")

            shutil.rmtree(pdf_dir,ignore_errors=True)
            shutil.rmtree(thumbnail_dir,ignore_errors=True)
            shutil.rmtree(img_dir,ignore_errors=True)
            
            os.makedirs(pdf_dir,exist_ok=True)
            os.makedirs(thumbnail_dir,exist_ok=True)
            os.makedirs(img_dir,exist_ok=True)

            st.success("system reset sucessfully")
            st.session_state.search_results = []

            st.session_state.reader_mode = False
            st.session_state.selected_doc = None
            st.session_state.current_page = 0

            init_db()
            st.rerun()

        else:
            st.error("Incorrect password")

tabs = st.tabs(["Upload", "Search and View", "Analytics"])

with tabs[0]:
    st.header("Upload PDF")
    pdf = st.file_uploader("Upload PDF",type="pdf")
    tags = st.text_input("Tags (Comma seperated)")
    description = st.text_area("Description")
    lecture_date = st.date_input("Lecture Date",value=None)
    
    if st.button("Uploaddd"):
        analytics_service.record_app_visit("upload click")
        if pdf:
            service.upload_doc(pdf, tags, description, lecture_date)
        else:
            st.error("Please upload pdf file")

with tabs[1]:
    st.header("Search & View")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Search by Tags")
        search_tag = st.text_input("Search by tag")

    with col2:
        st.subheader("Search by Date")
        search_by_date = st.date_input("Search by date",value=None)

    if st.button("Search"):
        analytics_service.record_app_visit("search click")
        st.session_state.search_results = service.search_doc(
            tags=search_tag if search_tag else None,
            date=str(search_by_date) if search_by_date else None
        )

    results = st.session_state.search_results

    if results and not st.session_state.reader_mode:
        st.subheader(f"Results: {len(results)} Document")

    for doc in results:

        col1, col2 = st.columns([1,3])

        with col1:
            st.image(doc.thumbnail_path, width=120)

        with col2:

            st.write(f"### {doc.name}")
            st.write(f"**Tags:** {doc.tags}")
            st.write(f"**Description:** {doc.description}")
            st.write(f"**Lecture Date:** {doc.lecture_date}")

            if st.button("Open", key=doc.id):
                analytics_service.record_app_visit("Open click")
                st.session_state.selected_doc = doc
                st.session_state.reader_mode = True
                st.session_state.current_page = 0
                st.rerun()

    if st.session_state.reader_mode and st.session_state.selected_doc:
        st.write("Reader Mode is active ")

        doc = st.session_state.selected_doc
        st.subheader(f"Reading: {doc.name}")
        folder_name = os.path.splitext(os.path.basename(doc.path))[0]
        image_dir = os.path.join("storage", "pdfs", folder_name)  # or "pdf" if that's where you save

        st.write("Document Path:", doc.path)
        st.write("Folder Name:", folder_name)
        st.write("Image Directory:", image_dir)
        st.write("Folder Exists:", os.path.exists(image_dir))

        if os.path.exists(image_dir):
            st.write("Files:", os.listdir(image_dir))

        if not os.path.exists(image_dir):
            st.error("Image not found, Image conversion fail")
        else:
            image = sorted(os.listdir(image_dir))

            total_pages = doc.total_pages
            current_page = st.session_state.current_page

            col0,col1,col2 = st.columns([1,3,1])

            with col0:
                if st.button("Previous") and current_page >0 :
                    analytics_service.record_app_visit("Previous click")
                    st.session_state.current_page-=1
                    st.rerun()

            with col2:
                if st.button("Next") and current_page < total_pages -1:
                    analytics_service.record_app_visit("Next click")
                    st.session_state.current_page+=1
                    st.rerun()


            img_path = os.path.join(image_dir,image[st.session_state.current_page])
            st.image(img_path,width="stretch")

            analytics_service.record_page_visit(doc.id,st.session_state.current_page )
            unique_page = analytics_service.get_unique_page_count(doc.id)
            progress = (unique_page/total_pages) * 100 if doc.total_pages else 0
            st.progress(progress/100)
            st.write(f"📖 Reading Progress: {progress:.1f}%")
            st.write(f"File Name: {doc.name}")


        if st.button("Close"):
            analytics_service.record_app_visit("Close click")
            st.session_state.reader_mode = False
            st.rerun()


with tabs[2]:
    st.header("Analytics")


    if st.button("Reset Analytics"):
        analytics_service.reset_analytics()
        st.success("Analytics reset sucessfull")


    st.subheader("App usage")

    app_data = analytics_service.get_app_visit()

    import pandas as pd

    df = pd.DataFrame(app_data,columns=["Event", "Count"])

    if df.empty:
        st.info("No analytics data yet. Perform some action to see insight")
    else:
        st.bar_chart(df.set_index("Event"))

    st.subheader("Document Progress")

    docs = service.get_all_doc()

    data = []

    for doc in docs:
        unique_page = analytics_service.get_unique_page_count(doc.id)
        progress = (unique_page/doc.total_pages) * 100 if doc.total_pages else 0

        data.append({
            "Document":doc.name,
            "Page Read":unique_page,
            "Total page":doc.total_pages,
            "Progress":round(progress,2)
        })

    df_doc = pd.DataFrame(data)
    st.dataframe(df_doc)