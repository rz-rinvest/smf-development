from CA.YahooFinance import TimeSplitter
from Models import ModelCreation
import pandas as pd
from datetime import *
from CA.configcontrol import ConfigControl

class ComparingTable:

  def Make(self,category):
    indexdf = pd.read_csv("CA/YahooFinance/processed/3moindex.csv")
    index = indexdf['index'].tolist()
    
    index.pop(0)
    outputindex = []
    outputindex.append(('ticker',False))
    outputindex.append(('pastdate',False))
    outputindex.append(('newdate',False))
    outputindex.append(('futuredate',False))
    
    for i in index:
      outputindex.append(("past_" + i,True))
      
    for i in index:
      outputindex.append(("new_" + i,True))
    
    data = []
    
    config = ConfigControl.ConfigControl()
    resultfunction = config.val.get("YF Model Creation Output Function")
    model = ModelCreation.ModelCreation(outputindex,resultfunction)
    files = TimeSplitter.Threemonthfiles()
   
    for k in range(len(files) - 1):
        print("Analysing changes between " + files[k] + " and " + files[k+1])
        df1 = pd.read_csv("CA/YahooFinance/processed/"+ category + "/" + files[k] + ".csv")
        df2 = pd.read_csv("CA/YahooFinance/processed/"+ category + "/" + files[k+1] + ".csv")

        tickerlist1 = []
        tickerlist2 = []

        for i in range(len(df1.columns)):
         tickerlist1.append(df1.iloc[0,i])

        for i in range(len(df2.columns)):
         tickerlist2.append(df2.iloc[0,i])
  
        intersection = self.Intersection(tickerlist1,tickerlist2)
        #print("Intersection: ")
        #print(intersection)
        
        for i in range(len(intersection)):
             #print("Calculating changes for " + intersection[i])
             ticker = intersection[i]
             case = model.NewCase()
             case.Set('pastdate',datetime.strptime(files[k], '%d-%m-%Y').strftime("%Y-%m-%d %H:%M:%S")      )
             case.Set('newdate',datetime.strptime(files[k+1], '%d-%m-%Y').strftime("%Y-%m-%d %H:%M:%S")       )
             case.Set('ticker',intersection[i])

             #print("Index in DF1  is " + str(self.GetTickerIndex(df1,ticker)))
             col1 = self.GetTickerIndex(df1,ticker)
             #print("Index in DF2  is " + str(self.GetTickerIndex(df2,ticker)))
             col2 = self.GetTickerIndex(df2,ticker)
             
             for i in range(len(index)):
                case.Set('past_' + index[i] , df1.iloc[i + 1,col1])
                case.Set('new_' + index[i] , df2.iloc[i + 1,col2])
             model.AddCase(case) 
                 
        
    
    
    abc = model.Printmodel()
    return abc

  
  def Intersection(self,arr1, arr2): 
    result = list(filter(lambda x: x in arr1, arr2))  
    return result
    
    
  def GetTickerIndex(self,df,ticker):
    tickerlist = []
    for i in range(len(df.columns)):
      if(df.iloc[0,i] == ticker):
        return i
    else:
      return False
    
