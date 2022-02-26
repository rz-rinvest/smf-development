import pandas as pd

class Exchanges:
  def __init__(self):
      self.data = pd.read_csv('Assets/Exchanges/config.csv')
      print(self.data)
    
  def GetDetails(self,exchange):
      config = pd.read_csv('Assets/Exchanges/config.csv')
      for i in range(len(config.index)):
        if(config.iloc[i, 0] == exchange):
           return config.iloc[i, 2],config.iloc[i, 3],config.iloc[i, 4].split(",")
      
