
import streamlit as st

from Projects.mockProjects import projects
from Utils.utils import render_component


@st.cache_data
def render_home():
    # =====================================================
    # CONFIG
    # =====================================================

    st.set_page_config(
        page_title="Trevor's Portfolio",
        layout="wide",
        page_icon=r".\images\my_log.png"
    )

    # =====================================================
    # HERO
    # =====================================================
    st.html(r'.\components\hero.html')


    # =====================================================
    # FEATURED PROJECT
    # =====================================================
    st.markdown('<div id="work"></div>', unsafe_allow_html=True)
    st.html(r'.\components\featured_card.html')


    # =====================================================
    # PROJECTS (ASYMMETRIC LAYOUT)
    # =====================================================

    st.markdown('<div class="section-title">Select Work', unsafe_allow_html=True)

    cols = st.columns(3)

    for idx, project in enumerate(projects):

        with cols[idx % 3]:
            st.html(
                render_component(
                    file_path=r".\components\project_card.html",
                    context=project
                )
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # =====================================================

    # ABOUT (METRICS)
    # =====================================================
    # st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
    st.html(r".\components\about.html")
    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # CONTACT
    # =====================================================
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.html(r'.\components\contact.html')
