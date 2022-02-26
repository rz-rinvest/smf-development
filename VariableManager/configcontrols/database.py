import pandas as pd

class database:

  def get(self,name):
    config = pd.read_csv('VariableManager/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         return config.iloc[i, 1]
    pass


  def update(self,name,val):
    config = pd.read_csv('VariableManager/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         config.iloc[i, 1 ] = val 
    config.to_csv('VariableManager/config.csv',index=False)



