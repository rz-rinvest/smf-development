import streamlit as st
import time
from Console import ConsoleFunctions

def app(conn):


  st.title('RINVEST')
  st.write(conn.status)

  if conn.status == False:
     if st.button('Start'):
        ConsoleFunctions.Start()    
     else:
        pass
   
  elif conn.status == True:
      st.write('RINVEST is already running .. ')    



