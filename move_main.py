
import streamlit as st

from css import css_sheet
from models import ProjectModel
from utils import render_component

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Trevor Portfolio",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown(body=css_sheet, unsafe_allow_html=True)
st.html(body=r'.\components\gemini_glow.html')
# =====================================================
# NAVBAR
# =====================================================

st.html(r'.\components\navbar.html')

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
projects = [
    ProjectModel(
        title="Text to SQL Agent",
        desc="An AI-powered agent that converts natural language into optimized SQL queries and executes them directly against a database. Designed to simplify data access, reduce query complexity, and enable non-technical users to interact with structured data efficiently."
    ),
    ProjectModel(
        title="Executive BI Dashboard",
        desc="A business intelligence dashboard built to track key performance indicators, monitor trends, and support executive-level decision-making. Includes dynamic visualizations and forecasting components for strategic planning."
    ),
    ProjectModel(
        title="SQL Cohort Analysis",
        desc="A structured retention analysis system using SQL window functions to segment users, track behavior over time, and measure cohort-based engagement and retention performance."
    ),
    ProjectModel(
        title="Fraud Detection System",
        desc="A machine learning pipeline designed to detect anomalous and potentially fraudulent activity using engineered features, behavioral patterns, and real-time scoring. Focused on scalable detection and reliable decision support in production-like environments."
    ),
    ProjectModel(
        title="Revenue Forecast Model",
        desc="A time-series forecasting system designed to predict future revenue trends based on historical data patterns. Helps support budgeting, planning, and financial decision-making with data-driven projections."
    ),
    ProjectModel(
        title="Data Analytics",
        desc="A general-purpose analytics workflow for extracting actionable insights from messy, unstructured datasets. Includes data cleaning, transformation, exploratory analysis, and insight generation for decision support."
    )
]



st.markdown('<div class="section-title">Select Work</div>', unsafe_allow_html=True)

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


# =====================================================

# ABOUT (METRICS)
# =====================================================
# st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
st.html(r".\components\metrics.html")
st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# CONTACT
# =====================================================
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.html(r'.\components\contact.html')
