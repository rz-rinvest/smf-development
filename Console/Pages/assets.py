from Console.Pages.assets_ import stocks
from Console.Pages.assets_ import crypto
import streamlit as st
from Assets import AssetManager

def app():
  am = AssetManager.AM()


  PAGES = {
    "Stocks": stocks,
    "Crypto" : crypto
  }

  selection = st.sidebar.selectbox('Welcome',list(PAGES.keys()))    
  page = PAGES[selection]
  jobids = page.app(am)
  
  
  return jobids



