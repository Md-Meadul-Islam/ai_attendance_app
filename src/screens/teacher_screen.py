import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    teacher_screen_login()

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace")
    st.header("Login using Password", text_alignment="center")
    st.space()
    st.space()

    user_name = st.text_input("Enter your name...", placeholder="Md. Meadul Islam")
    user_password = st.text_input("Enter your password...", placeholder="******", type="password")

    st.divider()
    footer_dashboard()


def teacher_screen_register():
    pass