import streamlit as st
import pandas as pd


def app():
  configfile  = "CA/config.csv"
  config = pd.read_csv(configfile)
  
  inputvals = []
  
  for i in range(len(config.index)):
    inputvals.append(st.text_input(config.iloc[i,0],config.iloc[i,1]))
  
  if st.button("Edit"):
     newconfig = pd.DataFrame({"key" : [] , "value" : []})
     for i in range(len(config.index)):
         df2 = {'key': config.iloc[i,0] , 'value': inputvals[i]}
         newconfig = newconfig.append(df2, ignore_index = True)
     newconfig.to_csv(configfile,index=False)
  
  
