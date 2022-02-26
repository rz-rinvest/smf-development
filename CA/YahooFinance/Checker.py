import yahoo_fin.stock_info as si
from Assets import AssetManager
from CA.configcontrol import ConfigControl
import streamlit as st
import pandas as pd
from datetime import *

maxdate = datetime.min
def checklastdate():
     am = AssetManager.AM()
     curdate = ConfigControl.ConfigControl().val.get("Present YF Date")
     st.write("Last Uploaded Date is " + curdate)
     global maxdate
     stocks = am.GetAllStocks()
     yfstocks = []
     for stock in stocks:
        if stock.yfverified == True and stock.yfstatus == "New":
          yfstocks.append(stock)
     
     data = pd.DataFrame([],columns=["Stock","Balance Sheet", "Cashflow Statement" , "Income Statement"])
     for stock in yfstocks:
       data.loc[len(data.index)] = [stock.name , "Updating" , "Updating" , "Updating"]
     
     with st.empty():
       st.dataframe(data)
       for i in range(len(yfstocks)):
         data.iloc[i,0] = yfstocks[i].name
         re = si.get_balance_sheet(yfstocks[i].yahoofinancename, yearly = False)
         redate = max(re.columns)
         maxdate = max([maxdate,redate])
         data.iloc[i,1] = redate
         st.dataframe(data)
         st.dataframe(data.style.applymap(color_negative_red, subset=["Balance Sheet", "Cashflow Statement" , "Income Statement"]))
       
         cf = si.get_cash_flow(yfstocks[i].yahoofinancename, yearly = False)
         cfdate = max(cf.columns)
         maxdate = max([maxdate,redate])
         data.iloc[i,2] = cfdate
         st.dataframe(data)
         st.dataframe(data.style.applymap(color_negative_red, subset=["Balance Sheet", "Cashflow Statement" , "Income Statement"]))
        
         ist= si.get_income_statement(yfstocks[i].yahoofinancename, yearly = False)
         isdate = max(ist.columns)
         maxdate = max([maxdate,redate])
         data.iloc[i,3] = isdate
         st.dataframe(data)
         st.dataframe(data.style.applymap(color_negative_red, subset=["Balance Sheet", "Cashflow Statement" , "Income Statement"]))
       
       
     st.write(maxdate)
       
def color_negative_red(value):
  if value == maxdate:
    color = 'green'
  else:
    color = 'red'

  return 'color: %s' % color  
       
       
       








       
       
    
