from Console.Pages import home
from Console.Pages import development
from Console.Pages import results
from Console.Pages import models
from Console.Pages import training
from Console.Pages import assets
from Console.Pages import timers
from Console.Pages import company
import time
import json
import streamlit as st
import sys

import StreamLitClient 
from Console import ConsoleFunctions



@st.cache(allow_output_mutation=True)
conn = StreamLitClient.divert("ca","Console")




def display(report):
  if report['type'] == "success":
    st.success(report['message'])
  elif report['type'] == "error":
    st.error(report['message'])
  elif report['type'] == "warning":
    st.warning(report['message'])
  elif report['type'] == "text":
    st.text(report['message'])
  else:
    st.write(report['message'])

PAGES = {
    "Home": home,
    "Development" : development,
    "Assets" : assets,
    "Company Analysis" : company,
    "Results" : results,
    "Models"  : models, 
    "Training"  : training,
    "Timers" : timers
}

st.sidebar.title('Navigation')
#selection = st.sidebar.radio("Go to", list(PAGES.keys()))
selection = st.sidebar.selectbox('Welcome',list(PAGES.keys()))    
page = PAGES[selection]
jobsids = page.app(conn)

'''
if :
  
  with st.empty():  
    while True:
      data = json.loads(conn.get("consoledata","{}"))
      st.write(data)
      reports = data['reports']
      placeholder = st.empty()
      if len(reports) >= 1:
        display(reports[len(reports) - 1 ])
      time.sleep(1)
  
'''







