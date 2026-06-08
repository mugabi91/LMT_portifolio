
import streamlit as st


# =====================================================
# CONTACT
# =====================================================
@st.cache_data
def render_contact():
    st.set_page_config(
        page_title="Trevor's Contact Page",
        layout="wide",
        page_icon=r".\images\my_log.png"
    )


    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.html(r'.\components\contact.html')
