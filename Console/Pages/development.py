import streamlit as st
from Console.Pages.development_ import workarea
from Console.Pages.development_ import reports

def app():
   
  PAGES = {
    "Work Area": workarea,
    "All Logs and Reports" : reports
  }

  selection = st.sidebar.selectbox('',list(PAGES.keys()))    
  page = PAGES[selection]
  jobids = page.app()

 


