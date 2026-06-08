
import streamlit as st

from models import ProjectModel
from utils import render_component


def render_learn():
    st.set_page_config(
        page_title="Trevor's Learn Page",
        layout="wide",
        page_icon=r".\images\my_log.png"
    )

    st.markdown("Hi there you have reached my LEARN page")