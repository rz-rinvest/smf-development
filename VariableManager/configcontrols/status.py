import pandas as pd

class status:

  def get(self,name):
    config = pd.read_csv('VariableManager/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         return config.iloc[i, 6]
    pass


  def update(self,name,val):
    config = pd.read_csv('VariableManager/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         config.iloc[i, 6] = val 
    config.to_csv('VariableManager/config.csv',index=False)



