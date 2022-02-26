import Variable
import streamlit as st
import sys
import time

def get(function,case):
  time.sleep(2)
  a = function.find("->",0,len(function))
  command = function[0:a]
  
  if command == "function":
    b = function.find("(",a,len(function)) + 1
    fname = function[a+2:b-1]
    c = function.rfind(")",b,len(function))
    data = function[b:c]
    datas = data.split(",")
    for i in range(len(datas)):
       datas[i] = get(datas[i],case)
       
       
    current_module = sys.modules[__name__]
    result = getattr(current_module, fname)(datas)
    return result
    
  if command == "rowvar":
    varname = function[a+2:len(function)] 
    st.write(varname)
    return case.Get(varname)
    









def Change(data):
  st.write(data)
  a = data[0]
  b = data[1]
  c = data[2]
  return 15 
  

def Databasename(data):
  a = data[0]
  return a 
  
