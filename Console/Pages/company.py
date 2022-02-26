import streamlit as st
from Console.Pages.company_ import dashboard
from Console.Pages.company_ import config


def app():

  PAGES = {
    "Dashboard": dashboard,
    "Configuration" : config
  }

  selection = st.sidebar.selectbox('',list(PAGES.keys()))    
  page = PAGES[selection]
  jobids = page.app()
  
