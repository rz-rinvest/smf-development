import yahoo_fin.stock_info as si
import pandas as pd
import os.path
from os import path
import csv
import numpy as np



def UpdateIndex(ind,dft):
  for i in range(len(dft)):
    if dft.index[i] in ind : 
     pass
    else:
      ind.append(dft.index[i])
def UpdateCols(cols,dft):
  for i in range(len(dft.columns)):
    datestring = dft.columns[i].to_pydatetime()
    date = datestring.strptime(str(datestring), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y")
    if date in cols : 
     pass
    else:
      cols.append(date)

def GetColIndex(name,dft):
  for i in range(len(dft.columns)):
    datestring = dft.columns[i].to_pydatetime()
    date = datestring.strptime(str(datestring), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y")
    if(name == date):
      return i
      break
  else:
    return None

def MakeNewRow(ind,bi,re,cf,ist,i):
  newrow = []
  for j in range (len(ind)):
    b = set(bi.index)
    r = set(re.index)
    c = set(cf.index)
    s = set(ist.index)
    if ind[j] in b:
      newrow.append(bi.loc[ind[j]][0])
    elif ind[j] in r:
      colno = GetColIndex(col[i],re)
      if(colno != None):
        newrow.append(re.loc[ind[j]][colno])
      else:
        return None
        break
    elif ind[j] in c:
      colno = GetColIndex(col[i],cf)
      if(colno != None):
        newrow.append(cf.loc[ind[j]][colno])
      else:
        return None
        break
    elif ind[j] in s:
      colno = GetColIndex(col[i],ist)
      if(colno != None):
        newrow.append(ist.loc[ind[j]][colno])
      else:
        return None
        break
    else:
      newrow.append(0)
      #print("Arrangement Error : " + ind[j] + " not found in any index")
  else:
    return newrow


def Process(ind,col,bi,re,cf,ist,ticker):
  for i in range(len(col)):
    filename = col[i]
    if(path.exists("raw/" + filename+ ".csv")):
      df = pd.read_csv("raw/" + filename + ".csv")
      if(TickerInData(df,ticker) == False):
        newrow = MakeNewRow(ind,bi,re,cf,ist,i)
        df.insert(len(df.columns),len(df.columns),newrow, True)
        df.to_csv( "raw/" + filename + ".csv",sep=',',index=False)
        #print("Updating " + filename)
      #display(df)
    else:
      newrow = MakeNewRow(ind,bi,re,cf,ist,i)
      if(newrow != None):
        newdf = pd.DataFrame(newrow,ind) 
        newdf.to_csv("raw/" +  col[i] + ".csv",sep=',',index=False)
        print("New Quarter file created " + col[i])


def TickerInData(df,ticker):
  tickerlist = []
  for i in range(len(df.columns)):
    tickerlist.append(df.iloc[0,i])
  if ticker in tickerlist:
    return True
  else:
    return False

tfc = pd.read_csv("tickers.csv")
tick = tfc['SYMBOL'].tolist()
listoftickers = []

for i in range(len(tick)):
  listoftickers.append(tick[i] + ".NS")

ind = []
col = []
bi = {}
re = {}
cf = {}
ist = {}

for i  in range(len(listoftickers)):
  print("Comparing Financials of " + listoftickers[i])
  try:
   bi[i] = pd.DataFrame([listoftickers[i]],['ticker'])
   re[i] = si.get_balance_sheet(listoftickers[i], yearly = False)
   cf[i] = si.get_cash_flow(listoftickers[i], yearly = False)
   ist[i] = si.get_income_statement(listoftickers[i], yearly = False)
  except:
   print(listoftickers[i] + " -  Not found")
  
  

for i in range(len(listoftickers)):
  try:
   UpdateIndex(ind,bi[i])
   UpdateIndex(ind,re[i])
   UpdateIndex(ind,cf[i])
   UpdateIndex(ind,ist[i])
   UpdateCols(col,re[i])
   UpdateCols(col,cf[i])
   UpdateCols(col,ist[i])
  except:
    pass

indexdict = {'index' : ind}
indexdf = pd.DataFrame(indexdict)
indexdf.to_csv("rawindex.csv",sep=',',index=False)

#print(ind)
#print(col)
#print(re.loc['totalLiab'][1])

for i in range(len(listoftickers)):
  print('Collecting ' + listoftickers[i])
  try:
    Process(ind,col,bi[i],re[i],cf[i],ist[i],listoftickers[i])
  except:
    pass


    

print("Please note down the index values")
print(ind)



