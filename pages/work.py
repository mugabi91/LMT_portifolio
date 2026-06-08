
import streamlit as st

from Projects.mockProjects import projects
from Utils.utils import render_component


@st.cache_data
def render_work():
    st.set_page_config(
        page_title="Trevor's Work Page",
        layout="wide",
        page_icon=r"./images/my_log.png"
    )

    # =====================================================
    # PROJECTS (ASYMMETRIC LAYOUT)
    # =====================================================

    st.markdown('<div class="section-title">Select Work', unsafe_allow_html=True)

    cols = st.columns(3)

    for idx, project in enumerate(projects):

        with cols[idx % 3]:
            st.html(
                render_component(
                    file_path=r"./components/project_card.html",
                    context=project
                )
            )

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================