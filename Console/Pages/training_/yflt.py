import streamlit as st
from Console import ConsoleFunctions


from CA import ca
from Assets import AssetManager
import time
from CA.YahooFinance import Checker
from datetime import datetime

def app():
  jobids  = []
  st.title("Yahoo Finance Company Analysis Data (CA)") 
  conn = Connection.Connection()
  if st.button('Import'):
      if ConsoleFunctions.Status(conn):
         jobid = conn.post("ca-yf-check","{}")
         jobids.append(jobid)
      else:
         st.warning("Please start the software")
  
  
  Checker.checklastdate()


  return jobids
     
    
     
