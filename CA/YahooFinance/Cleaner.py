import pandas as pd
import numpy as np
from CA.YahooFinance import PercentageFinder
from CA.Models.configcontrol import ConfigControl

class Cleaner:
  
  
    def __init__(self):
      from CA.YahooFinance import TimeSplitter
    
      self.Threefiles = TimeSplitter.Threemonthfiles()
      self.Sixfiles = TimeSplitter.Sixmonthfiles()
      self.index = TimeSplitter.rawindex()
      
      self.curfiles = self.Threefiles       
      pf = PercentageFinder.PercentageFinder()
      pn = pf.Plot(self,100,0,0,1,[])['percentage']
      print("Perfect percentage is " + str(pn))
      
      self.main(self.Threefiles,self.index,"3mo",pn)
      
      
      self.curfiles = self.Sixfiles       
      pf = PercentageFinder.PercentageFinder()
      pn = pf.Plot(self,100,0,0,1,[])['percentage']
      print("Perfect percentage is " + str(pn))
      
      self.main(self.Sixfiles,self.index,"6mo",pn)
     
      


    def main(self,listoffiles,index,category,pn):
      percentagenormaliser = pn
      rowstodelete = []
      df = {}
    
      for i in range(len(listoffiles)):
        filename = listoffiles[i]
        df[i] = pd.read_csv("CA/YahooFinance/storage/values/" + filename + ".csv")
    
      rowstodelete = self.ProcessRow(df,index,percentagenormaliser)
      #print(str(len(index)) + "il " + str(len(rowstodelete)) + " index delete cheyum")
      index = self.DeleteRowsfromDataSets(df,rowstodelete,index)
    
      countfordisplay = 0
      totalcolumncount = 0
      for j in range(len(df)):
        colstodelete = []
        totalcolumncount = totalcolumncount + len(df[j].columns)
        for i in range(len(df[j].columns)):
         col  = df[j][df[j].columns[i]].tolist()
         if(self.CheckNullinList(col)):
          colstodelete.append(i)
          countfordisplay = countfordisplay + 1
        df[j]= df[j].drop(df[j].columns [ colstodelete ], axis = 1)
       
      #print(str(totalcolumncount) + "il " + str(countfordisplay) + " stock data delete cheyum")
      indexdict = {'index' : index}
      indexdf = pd.DataFrame(indexdict)
      indexdf.to_csv("CA/YahooFinance/processed/" + category + "index.csv",sep=',',index=False)
 
      
    
      for j in range(len(df)):
        df[j].reset_index(drop=True, inplace=True)
        df[j].columns = range(df[j].shape[1])
        #display(df[j])
        df[j].to_csv("CA/YahooFinance/processed/" + category + "/" + listoffiles[j] + ".csv",sep=',',index=False)
      
      mc = ConfigControl.ConfigControl()
      return mc.PossibleNewModel(index,category)

    
    def ProcessRow(self,df,index,percentagenormaliser):
      lengthcount = []
      nullcount = []
      percentagecollection  = []
      for i in range(len(index)):
        lengthcount.append(0)
        nullcount.append(0)
        percentagecollection.append(0)
    
      for k in range(len(df)):
        #print(str(len(df)) + "il " + str(k) + " ennam theernu")
        for i in range(len(index)):
          lengthcount[i] = lengthcount[i] + len(df[k].columns)
        for i in range(len(df[k].columns)):
         for j in range(len(index)):
          if(self.IsNull(df[k].iloc[j,i])):
            nullcount[j] = nullcount[j] + 1
        rowstodelete = []
        for i in range(len(index)):
          percentagecollection[i] = (nullcount[i] / lengthcount[i]) * 100
          if(percentagecollection[i] > percentagenormaliser):
            rowstodelete.append(i)
      
      return rowstodelete
   
   
    def DeleteRowsfromDataSets(self,df,rowstodelete,index):
      for i in range(len(df)):
        df[i]= df[i].drop(df[i].index [ rowstodelete ])
      newindex = index.copy()
      for i in range(len(rowstodelete)):
        rownametodelete = index[rowstodelete[i]] 
        newindex.remove(rownametodelete)
      return newindex
    
    def CheckNullinList(self,row):
      for i in range(len(row)):
        if(self.IsNull(row[i])):
          return True
      else:
        return False


    def IsNull(self,val):
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
        
    def demo(self,listoffiles,index,pn):
      percentagenormaliser = pn
      rowstodelete = []
      df = {}
      for i in range(len(listoffiles)):
        filename = listoffiles[i]
        df[i] = pd.read_csv("CA/YahooFinance/storage/values/" + filename + ".csv")
    
      rowstodelete = self.ProcessRow(df,index,percentagenormaliser)
      #print(str(len(index)) + "il " + str(len(rowstodelete)) + " index delete cheyum")
      index = self.DeleteRowsfromDataSets(df,rowstodelete,index)
      countfordisplay = 0
      totalcolumncount = 0
      for j in range(len(df)):
        colstodelete = []
        totalcolumncount = totalcolumncount + len(df[j].columns)
        for i in range(len(df[j].columns)):
         col  = df[j][df[j].columns[i]].tolist()
         if(self.CheckNullinList(col)):
          colstodelete.append(i)
          countfordisplay = countfordisplay + 1
        df[j]= df[j].drop(df[j].columns [ colstodelete ], axis = 1)
       
      #print(str(totalcolumncount) + "il " + str(countfordisplay) + " stock data delete cheyum")
      datacount =  (len(index)) * (totalcolumncount - countfordisplay)

      return datacount        
        
        
