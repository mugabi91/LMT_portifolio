import streamlit as st

from css import css_sheet
from pages.about import render_about
from pages.contact import render_contact
from pages.home import render_home
from pages.Learn.R_progamming import render_r_programming
from pages.work import render_work


def main():
    
    st.set_page_config(
        page_title="Trevor's Portfolio",
        layout="wide",
        page_icon=r".\images\my_log.png"
    )
    ### inject css and style
    st.markdown(css_sheet, unsafe_allow_html=True)
    st.html(r".\components\gemini_glow.html")
    
    ## nav  bar
    st.html(r".\components\navbar.html")

    current_page = st.query_params.get("page", "home")

    pages = {
        "home": render_home,
        "work": render_work,
        "learn": render_r_programming,
        "contact": render_contact,
        "about": render_about,
    }
    
    st.markdown(
    '<div class="page-content">',
    unsafe_allow_html=True)

    pages.get(current_page, render_home)()
    
    st.markdown(
    '</div>',
    unsafe_allow_html=True)

if __name__ == "__main__":
    main()