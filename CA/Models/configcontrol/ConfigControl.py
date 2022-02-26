import pandas as pd
from CA.Models.configcontrol import index
from CA.Models.configcontrol import status
from CA.Models.configcontrol import timeframe

class ConfigControl:

  def __init__(self):
    try:
      config = pd.read_csv('CA/Models/config.csv')
    except:
      dicter = {'Model Name' : [] , 'index' : [] , 'status' : [] , 'timeframe' : []  }
      config = pd.DataFrame(dicter)
      config.to_csv('CA/Models/config.csv' ,index=False)
    self.Functions()
 

  def new(self,name,index,status,timeframe):
    config = pd.read_csv('CA/Models/config.csv')
    indexlist = ",".join(index)
    config.loc[len(config.index)] = [name,indexlist,status,timeframe]
    config.to_csv('CA/Models/config.csv',index=False)


  def display(self):
    print(pd.read_csv('CA/Models/config.csv'))
  def get(self):
    return pd.read_csv('CA/Models/config.csv')
    
  def PossibleNewModel(self,index,timeframe):
    df = self.get()
    for i in range(len(df.loc[:,"index"])):
      cind = df.iloc[i,1].split(",")
      if(set(index) == set(cind)):
         print("Found one model with same index")
         return df.iloc[i,0]
    else:
      self.new(len(df.loc[:,"index"]),index,"Processed",timeframe)
      print("New Model")
      return len(df.loc[:,"index"])

  def Functions(self):
    self.index = index.index()
    self.status = status.status()
    self.timeframe = timeframe.timeframe()
    
    
    
    
    
    
    
    
    
    
    
    
