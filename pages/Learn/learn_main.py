
# LEARN LAND PAGE
# =====================================================

import streamlit as st


@st.cache_data
def render_learn_main():
    st.set_page_config(
        page_title="Learning Page",
        layout="wide",
        page_icon=r".\images\my_log.png"
    )

    # st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
    st.write("hi main learn page")
    st.markdown("<br>", unsafe_allow_html=True)
