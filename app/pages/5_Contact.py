import streamlit as st

st.set_page_config(page_title="Contact — WITIN", layout="wide")
st.title("Contact")

with st.form("contact"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("What do you want to track?")
    submitted = st.form_submit_button("Send")

if submitted:
    st.success("Received. (Phase 2: wire this to email/DB.)")

st.markdown("Or email directly: **mailto:huyentr246@gmail.com**")
