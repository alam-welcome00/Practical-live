# streamlit run streamlit_learn.py
import streamlit as st

st.set_page_config(
    page_title="streamlit demo app",
    page_icon="🚀",
    # layout="wide",
    layout="centered"
)

# <h1>
st.title("Ultimate Data Science")

# <h3>
st.subheader("Level 1")

# <p>
st.write("This is batch number 2 of ultimate data science bootcamp")

# Tabs
tab1, tab2, tab3 = st.tabs(["Home", "Dashboard", "Settings"])

with tab1:
    # print("Welcome to home tab")
    st.write("Welcome to Home tab!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Left section (HOME)!")
        st.button("Click Left Section Button", type="primary")

    with col2:
        st.write("Centre section (HOME)!")
        st.button("Click Centre Section Button", type="secondary")

    with col3:
        st.write("Right section (HOME)!")
        st.button("Click Right Section Button", type="tertiary")

with tab2:
    st.write("Welcome to Dashboard tab!")

with tab3:
    st.write("Welcome to Settings tab!")

st.divider()

st.subheader("Level 2")

# container
with st.container(height=200, border=True,HorizontalAlignment = "right",
):
    for i in range(100):
        st.write(f"Hello {i}")

st.divider()

st.subheader("Level 3 - Widgets")

# input widgets

if st.button("Say Hello"):
    st.write("Hello there!")

st.link_button("Streamlit Widget Page Redirect", url="https://docs.streamlit.io/develop/api-reference/widgets")

a = 0
print(a)
name = st.text_input("Enter Name")
a+=1
print(a)
print(name)
st.write(f"Hello {name}!")

count = 0
if st.button("Click here to add 1 to the count"):
    count+=1
    st.write(f"Hello there!, the current count value is {count}")


u_name = st.text_input("User Name")
p_u_name = st.text_input("Password", type="password")
bio = st.text_area("Tell us about yourself", height=100)

st.subheader("Level 4 - Widgets")

import datetime
today = datetime.date.today()

picked_date = st.date_input("Pick a date", today)
st.write(picked_date)

st.divider()

uploaded_file = st.file_uploader("Upload a csv", type=["csv", "txt"])

from io import StringIO

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # df = pd.read_csv(uploaded_file)
    string_data = stringio.read()
    
    st.write(f"{type(uploaded_file)}")
    st.write(f"{type(string_data)}")

    st.write(f"File Contents :")
    st.code(string_data, language="text")
    # st.write("File Uploaded!!")
    st.success("File Uploaded!!")

st.warning("File loading warning!")
st.error("Error!")
st.info("Here is a helpful tip!")


st.divider()

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

st.divider()

st.title("Main Title") # Large
st.header("Section Header") # Medium
st.subheader("Sub-section") # Small

st.markdown("We have **bold** in this statement.")

st.markdown("<h1 style='color: blue;'>Custom html</h1>", unsafe_allow_html=True)

st.divider()

st.subheader("Level 5 - Extra")

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.write("Streamlit Dataframe visualization")
st.dataframe(df)

st.write("Streamlit Dataframe barchart")
st.bar_chart(df)

# image
st.image(r"C:\Users\scl\Downloads\Downloads-Cleaned(13226)\wallpaper\wallhaven.png", caption="My Image", width=300)

st.divider()

import time
bar = st.progress(0)
for percent in range(100):
    time.sleep(0.1)
    bar.progress(percent + 1)

st.divider()

text_to_save = "1,2,3,4,5"
st.download_button(
    label="Download text file",
    data=text_to_save,
    file_name="dummy_csv.txt",
    mime="text/plain"
)