import streamlit as st

st.set_page_config(
    page_title="streamlit demo app",
    page_icon="🚀",
    layout="centered"
)

st.title("Ultimate Data Science")
st.header("Sameer")
st.subheader("Level 1")

tab_1, tab_2, tab_3 = st.tabs(['Home', "Dashboard","Setting"])

with tab_1:
    st.write("Welcome in the Home tab")
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

with tab_2:
    st.write("Welcome to Dashboard tab!")

with tab_3:
    st.write("Welcome to Settings tab!")

st.divider()

st.subheader("Level 2")

with st.container(height=200, border=True,horizontal_alignment = "right"):
    for i in range(100):
        st.write(f"Hello {i}")

st.divider()

st.subheader("Level 3 - Widgets")

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
