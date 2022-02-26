import pandas as pd

class ClsData:
  def __init__(self):
    try:
      config = pd.read_csv('Console/config.csv')
    except:
      dicter = {'key' : ['MLExponentialFactor','MLMultiplierFactor','MLAdditionalConstant'] , 'value' : [0,0,0] }
      config = pd.DataFrame(dicter)
      config.to_csv('Console/config.csv' ,index=False)
 
  def get(self,name):
    
    config = pd.read_csv('Console/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         return config.iloc[i, 1]
    pass


  def update(self,name,val):
    config = pd.read_csv('Console/config.csv')
    for i in range(len(config.index)):
      if(config.iloc[i, 0] == name):
         config.iloc[i, 1] = val 
    config.to_csv('Console/config.csv',index=False)

  def new(self,name):
    config = pd.read_csv('config.csv')
    config.loc[len(config.index)] = [name , 0]
    config.to_csv('Console/config.csv',index=False)


  def display(self):
    print(pd.read_csv('Console/config.csv'))


cls = ClsData()
