import streamlit as st
from Assets import AssetObject


def booltostr(booler):
    if booler == True:
        return "Yes"
    elif booler == False:
        return "No"
    else:
        pass

def app(asset,am):
    name = asset.name
    editname = st.text_input("Asset Name(Primary Key)",name)
    exchange = asset.exchange
    editexchange = st.text_input("Exchange",exchange)
    databasename = asset.databasename
    editdatabasename = st.text_input("SQL Database Name",databasename)
    assettype = asset.assettype
    edittype = st.text_input("Asset Type",assettype)
    
    try:
      yfname = asset.yahoofinancename
      edityfname = st.text_input("Yahoo Finance API Name",yfname)

      yfverified = asset.yfverified
      edit_yfverified = st.checkbox("Is Company Details Verified",yfverified)

      yfstatus = asset.yfstatus
      edit_yfstatus = st.text_input("Yahoo Finance Management Status",yfstatus)
    except:
      pass
      
      
    
    if st.button("Done"):  
      editedasset = AssetObject.AssetObject(editname,editexchange,edittype,editdatabasename)
      try:
         editedasset.YahooFinanceName(edityfname)
         editedasset.YahooFinanceGenuine(booltostr(edit_yfverified))
         editedasset.YahooFinanceStatus(edit_yfstatus)
      except:
         pass
      am.Update([editedasset])
      return False

    return True  
      
      
      
