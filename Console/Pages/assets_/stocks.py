from Console.Pages.assets_ import edit
import streamlit as st



editing = False

def app(am):
  global editing
  configfile  = "Assets/stocksconfig.csv"
  st.table(am.stocksc)
  stocks = []
  for asset in am.assets:
    if asset.assettype == "Stocks":
      stocks.append(asset.name)
  option = st.selectbox('Select a Stock to edit', stocks)
  if editing or st.button("Edit"):
     editing = edit.app(am.assets[am.FindStockIndexbyName(option)],am)

  pass

