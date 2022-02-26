import yahoo_fin.stock_info as si
import pandas as pd
import os.path
from os import path
import csv
import numpy as np


class YF_Import:
    tickers = []
    names = []
    
    def __init__(self,stocks):
      for stock in stocks:
       self.tickers.append(stock.yahoofinancename) 
       self.names.append(stock.name)    
       
      ind = []
      self.col = []
      bi = {}
      re = {}
      cf = {}
      ist = {}
      self.notavailiblestocks = []
      self.collectedstocks = []
      
      for i  in range(len(self.tickers)):
        print("Comparing Financials of " + self.tickers[i])
        try:
          bi[i] = pd.DataFrame([self.names[i]],['ticker'])
          re[i] = si.get_balance_sheet(self.tickers[i], yearly = False)
          cf[i] = si.get_cash_flow(self.tickers[i], yearly = False)
          ist[i] = si.get_income_statement(self.tickers[i], yearly = False)
          self.collectedstocks.append(stocks[i])
        except:
          self.notavailiblestocks.append(stocks[i])
     
     
      for i in range(len(self.tickers)):
         try:
           self.UpdateIndex(ind,bi[i])
           self.UpdateIndex(ind,re[i])
           self.UpdateIndex(ind,cf[i])
           self.UpdateIndex(ind,ist[i])
           self.UpdateCols(self.col,re[i])
           self.UpdateCols(self.col,cf[i])
           self.UpdateCols(self.col,ist[i])
         except:
           print("Error in updating Part of Index and Column in CA Line 46 - CA/YahooFinance/Importer")
           pass
      
      print("You are going to update the Company Analysis Data - This process is irreversible (Make sure the data is verified) (Y/N) ")
      choice = str(input())
      if(choice == 'N'):
         return None
           
      indexdict = {'index' : ind}
      indexdf = pd.DataFrame(indexdict)
      indexdf.to_csv("CA/YahooFinance/storage/rawindex.csv",sep=',',index=False)
      
      for i in range(len(self.tickers)):
         print('Collecting ' + self.tickers[i])
         try:
            self.Process(ind,self.col,bi[i],re[i],cf[i],ist[i],self.tickers[i])
         except Exception as e:
            print("There is an error in storing Yahoo Import - Check Process definintion in YF Importer.py")
            print(e)
            
    def returner(self):
      return {"Imported" : self.collectedstocks , "NAStocks" : self.notavailiblestocks}

    def UpdateIndex(self,ind,dft):
      for i in range(len(dft)):
        if dft.index[i] in ind : 
         pass
        else:
          ind.append(dft.index[i])
    def UpdateCols(self,cols,dft):
      for i in range(len(dft.columns)):
        datestring = dft.columns[i].to_pydatetime()
        date = datestring.strptime(str(datestring), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y")
        if date in cols : 
         pass
        else:
          cols.append(date)
          
          
    
    def Process(self,ind,col,bi,re,cf,ist,ticker):
      for i in range(len(col)):
        filename = col[i]
        if(path.exists("CA/YahooFinance/storage/values/" + filename+ ".csv")):
          df = pd.read_csv("CA/YahooFinance/storage/values/" + filename + ".csv")
          if(self.TickerInData(df,ticker) == False):
            newrow = self.MakeNewRow(ind,bi,re,cf,ist,i)
            df.insert(len(df.columns),len(df.columns),newrow, True)
            df.to_csv( "CA/YahooFinance/storage/values/" + filename + ".csv",sep=',',index=False)
            #print("Updating " + filename)
          #display(df)
        else:
          newrow = self.MakeNewRow(ind,bi,re,cf,ist,i)
          if(newrow != None):
            newdf = pd.DataFrame(newrow,ind) 
            newdf.to_csv("CA/YahooFinance/storage/values/" +  col[i] + ".csv",sep=',',index=False)
            print("New Quarter file created " + col[i])


    def GetColIndex(self,name,dft):
      for i in range(len(dft.columns)):
        datestring = dft.columns[i].to_pydatetime()
        date = datestring.strptime(str(datestring), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y")
        if(name == date):
          return i
          break
      else:
        return None

    def MakeNewRow(self,ind,bi,re,cf,ist,i):
      newrow = []
      for j in range (len(ind)):
        b = set(bi.index)
        r = set(re.index)
        c = set(cf.index)
        s = set(ist.index)
        if ind[j] in b:
          newrow.append(bi.loc[ind[j]][0])
        elif ind[j] in r:
          colno = self.GetColIndex(self.col[i],re)
          if(colno != None):
            newrow.append(re.loc[ind[j]][colno])
          else:
            return None
            break
        elif ind[j] in c:
          colno = self.GetColIndex(self.col[i],cf)
          if(colno != None):
            newrow.append(cf.loc[ind[j]][colno])
          else:
            return None
            break
        elif ind[j] in s:
          colno = self.GetColIndex(self.col[i],ist)
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
        
    
    def TickerInData(self,df,ticker):
      tickerlist = []
      for i in range(len(df.columns)):
        tickerlist.append(df.iloc[0,i])
      if ticker in tickerlist:
        return True
      else:
        return False
    





  
  
