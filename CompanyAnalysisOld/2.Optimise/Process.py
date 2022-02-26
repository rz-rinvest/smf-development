import pandas as pd
import csv
import numpy as np

#FUNCTIONS BEGIN

def IsNull(val):
  if isinstance(val,float):
    if np.isnan(val):
      return True
  else:
    try:
      if float(val) == 0:
        return True
    except ValueError as ve:
      pass

    if(val == 0 or val == None or val == "NaN"):
      return True
  return False

def ProcessRow(df,index,percentagenormaliser):
  lengthcount = []
  nullcount = []
  percentagecollection  = []
  for i in range(len(index)):
    lengthcount.append(0)
    nullcount.append(0)
    percentagecollection.append(0)

  for k in range(len(df)):
    print(str(len(df)) + "il " + str(k) + " ennam theernu")
    for i in range(len(index)):
      lengthcount[i] = lengthcount[i] + len(df[k].columns)
    for i in range(len(df[k].columns)):
     for j in range(len(index)):
      if(IsNull(df[k].iloc[j,i])):
        nullcount[j] = nullcount[j] + 1
    rowstodelete = []
    for i in range(len(index)):
      percentagecollection[i] = (nullcount[i] / lengthcount[i]) * 100
      if(percentagecollection[i] > percentagenormaliser):
        rowstodelete.append(i)
  
  return rowstodelete

def DeleteRowsfromDataSets(df,rowstodelete,index):
  for i in range(len(df)):
    df[i]= df[i].drop(df[i].index [ rowstodelete ])
  newindex = index.copy()
  for i in range(len(rowstodelete)):
    rownametodelete = index[rowstodelete[i]] 
    newindex.remove(rownametodelete)
  return newindex

def CheckNullinList(row):
  for i in range(len(row)):
    if(IsNull(row[i])):
      return True
  else:
    return False


def Intersection(arr1, arr2): 
  result = list(filter(lambda x: x in arr1, arr2))  
  return result

def GetTickerIndex(df,ticker):
  tickerlist = []
  for i in range(len(df.columns)):
    if(df.iloc[0,i] == ticker):
      return i
  else:
    return False
    



def main(listoffiles,index,category,pn):
  
  
  percentagenormaliser = pn


  rowstodelete = []
  df = {}

  for i in range(len(listoffiles)):
    filename = listoffiles[i]
    df[i] = pd.read_csv("raw/" + filename + ".csv")

  rowstodelete = ProcessRow(df,index,percentagenormaliser)
  print(str(len(index)) + "il " + str(len(rowstodelete)) + " index delete cheyum")
  index = DeleteRowsfromDataSets(df,rowstodelete,index)

  countfordisplay = 0
  totalcolumncount = 0
  for j in range(len(df)):
    colstodelete = []
    totalcolumncount = totalcolumncount + len(df[j].columns)
    for i in range(len(df[j].columns)):
     col  = df[j][df[j].columns[i]].tolist()
     if(CheckNullinList(col)):
      colstodelete.append(i)
      countfordisplay = countfordisplay + 1
    df[j]= df[j].drop(df[j].columns [ colstodelete ], axis = 1)
   
  print(str(totalcolumncount) + "il " + str(countfordisplay) + " stock data delete cheyum")
  print("Save cheyano ? (Y or N): ")
  choice = str(input())
  if(choice == 'N'):
    exit()
  
    

  for j in range(len(df)):
    df[j].reset_index(drop=True, inplace=True)
    df[j].columns = range(df[j].shape[1])
    #display(df[j])
    df[j].to_csv("processed/" + category + "/" + listoffiles[j] + ".csv",sep=',',index=False)
  
