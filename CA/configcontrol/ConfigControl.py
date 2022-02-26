import pandas as pd
from CA.configcontrol import key
from CA.configcontrol import val

class ConfigControl:

  def __init__(self):
    try:
      config = pd.read_csv('CA/config.csv')
    except:
      dicter = {'key' : ['Current Operation'] , 'val' : ['']}
      config = pd.DataFrame(dicter)
      config.to_csv('CA/config.csv' ,index=False)
    self.Functions()
 

  def new(self,name,index,status,timeframe):
    config = pd.read_csv('CA/config.csv')
    indexlist = ",".join(index)
    config.loc[len(config.index)] = [name,indexlist,status,timeframe]
    config.to_csv('CA/config.csv',index=False)


  def display(self):
    print(pd.read_csv('CA/config.csv'))
  def get(self):
    return pd.read_csv('CA/config.csv')
    
  

  def Functions(self):
    self.key = key.key()
    self.val = val.val()

    
    
    
    
    
    
    
    
    
    
    
    
