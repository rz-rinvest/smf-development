import pandas as pd

class status:

  def get(self,name):
    config = pd.read_csv('CA/Models/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         return config.iloc[i, 2].split(",")
    pass


  def update(self,name,val):
    val = ','.join(val)
    config = pd.read_csv('CA/Models/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         config.iloc[i, 2] = val 
    config.to_csv('CA/Models/config.csv',index=False)



