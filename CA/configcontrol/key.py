import pandas as pd

class key:

  def get(self,name):
    config = pd.read_csv('CA/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         return config.iloc[i, 0]
    pass


  def update(self,name,val):
    config = pd.read_csv('CA/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         config.iloc[i, 0] = val 
    config.to_csv('CA/config.csv',index=False)



