import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

image = Image.open('img/Walter White.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "img", "heisenberg.svg")
pages = [" ",'Home','Project1', 'Project2', 'Project3']

styles = {
    "nav": {
        "background-color": "rgb(34, 45, 50)",  # Darker background for a sleek look
    },
    "div": {
        "max-width": "36rem",  # Slightly wider for a more spacious layout
    },
    "span": {
        "border-radius": "0.75rem",  # Softer rounded edges
        "color": "rgb(210, 210, 210)",  # Light grey color for readability
        "margin": "0 0.25rem",  # Increased margin for more spacing between items
        "padding": "0.5rem 0.75rem",  # Larger padding for a comfortable click area
    },
    "img": {
        "border-radius": "0.25rem",  # Slight rounding on image corners
        "width": "80px",  # Moderate width for a small logo or icon
        "height": "auto",  # Maintain aspect ratio
        "margin": "0.25rem",  # Spacing around the image
    },
    "active": {
        "background-color": "rgba(50, 150, 255, 0.3)",  # Subtle blue background for active item
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",  # Light overlay effect on hover
    },
}

options = {
    "show_menu": False,
    "show_sidebar": True,
}

page = st_navbar(pages,
    styles=styles,
    logo_path=logo_path,
    options=options)

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