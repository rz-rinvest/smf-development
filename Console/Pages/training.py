from Console.Pages.training_ import yflt
import streamlit as st

def app():
  
  PAGES = {
    "Yahoo Finance (Long term)": yflt
  }

  selection = st.sidebar.selectbox('',list(PAGES.keys()))    
  page = PAGES[selection]
  jobids = page.app()
  
  
  return jobids






