import pandas as pd
from Assets import AssetObject

class AM:
  assets  = []
   
  def __init__(self):
    self.cryptoc = pd.read_csv('Assets/cryptoconfig.csv')
    self.stocksc = pd.read_csv('Assets/stocksconfig.csv')
    for i in range(len(self.stocksc.index)):
      name = self.stocksc.iloc[i,0]
      if self.checkduplicate(name):
         break
      exchange = self.stocksc.iloc[i,1]
      databasename = self.stocksc.iloc[i,2]
      s = AssetObject.AssetObject(name,exchange,"Stocks",databasename)
      s.YahooFinanceName(self.stocksc.iloc[i,3])
      s.YahooFinanceGenuine(self.stocksc.iloc[i,4])
      s.YahooFinanceStatus(self.stocksc.iloc[i,5])
      self.assets.append(s)
      
    for i in range(len(self.cryptoc.index)):
      name = self.cryptoc.iloc[i,0]
      if self.checkduplicate(name):
         break
      exchange = self.cryptoc.iloc[i,1]
      databasename = self.cryptoc.iloc[i,2]
      s = AssetObject.AssetObject(name,exchange,"Crypto",databasename)
      self.assets.append(s)
     
   

    
  def Update(self,assets):
    for asset in assets:
      if asset.assettype == "Stocks":
        self.stocksc = pd.read_csv('Assets/stocksconfig.csv')
        index = self.FindStockIndexbyName(asset.name)
        self.stocksc.iloc[index,0] = asset.name
        self.stocksc.iloc[index,1] = asset.exchange
        self.stocksc.iloc[index,2] = asset.databasename
        self.stocksc.iloc[index,3] = asset.GetStatus()
        self.stocksc.iloc[index,4] = asset.yahoofinancename
        self.stocksc.iloc[index,5] = asset.GetYFGenuine()
        self.stocksc.iloc[index,6] = asset.yfstatus
        self.stocksc.to_csv('Assets/stocksconfig.csv',index=False)
      else:
        pass
    
    
        
        
  def FindStockIndexbyName(self,name):
     for i in range(len(self.stocksc.index)):
       if self.stocksc.iloc[i,0] == name:
         return i
     else:
       print("No Stock found in database to update")
       return None    
       

  def GetAllStocks(self):
    assets = []
    for i in range(len(self.assets)):
      if self.assets[i].assettype == "Stocks":
         assets.append(self.assets[i])
    return assets
  
  def checkduplicate(self,name):
    for asset in self.assets:
        if asset.name == name:
          return True
    else:
       return False      
  
    
#When creating Inserting Feature be carefull that there is no ID stock name is primary key , do not allow to duplicate






   

