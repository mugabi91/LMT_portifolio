# ABOUT (METRICS)
# =====================================================

import streamlit as st


def render_about():
    st.set_page_config(
        page_title="Trevor's About Page",
        layout="wide",
        page_icon=r".\images\my_log.png"
    )

    # st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
    st.html(r".\components\metrics.html")
    st.markdown("<br>", unsafe_allow_html=True)
