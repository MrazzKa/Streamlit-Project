import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

# Load and set the favicon image for the app
image = Image.open('img/Walter White.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

# Define the logo path and pages
logo_path = os.path.join(os.path.dirname(__file__), "img", "heisenberg.svg")
pages = [" ", 'Home', 'Project1', 'Project2', 'Project3']

# Define navbar styles
styles = {
    "nav": {
        "background-color": "rgb(34, 45, 50)",
    },
    "div": {
        "max-width": "36rem",
    },
    "span": {
        "border-radius": "0.75rem",
        "color": "rgb(210, 210, 210)",
        "margin": "0 0.25rem",
        "padding": "0.5rem 0.75rem",
    },
    "img": {
        "border-radius": "0.25rem",
        "width": "80px",
        "height": "auto",
        "margin": "0.25rem",
    },
    "active": {
        "background-color": "rgba(50, 150, 255, 0.3)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",
    },
}

# Define navbar options
options = {
    "show_menu": False,
    "show_sidebar": True,
}

# Display navbar and set active page
page = st_navbar(
    pages,
    styles=styles,
    logo_path=logo_path,
    options=options
)

# Render the selected page
if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()
