import streamlit as st

from css import css_sheet
from pages.about import render_about
from pages.contact import render_contact
from pages.home import render_home
from pages.Learn import render_learn
from pages.work import render_work


def main():

    st.markdown(css_sheet, unsafe_allow_html=True)

    st.html(r".\components\gemini_glow.html")
    st.html(r".\components\navbar.html")

    current_page = st.query_params.get("page", "home")

    pages = {
        "home": render_home,
        "work": render_work,
        "learn": render_learn,
        "contact": render_contact,
        "about": render_about,
    }

    pages.get(current_page, render_home)()


if __name__ == "__main__":
    main()