class AssetObject:

  def __init__(self,name,exchange,assettype,databasename):
     self.name = name
     self.exchange = exchange
     self.databasename = databasename
     self.assettype = assettype
    
     


  
   
       

  #For Stocks
  
  def YahooFinanceName(self,name):
    self.yahoofinancename = name
    
  def YahooFinanceGenuine(self,name):
    self.yfverified = self.strtobool(name)

  
  def GetYFGenuine(self):
    return self.booltostr(self.yfverified)
       
  def YahooFinanceStatus(self,name):
    self.yfstatus = name
    

#Additional Functionalities   
     
       
  def booltostr(self,booler):
    if booler == True:
        return "Yes"
    elif booler == False:
        return "No"
    else:
        pass
  
  def strtobool(self,strer):
    if strer == "Yes":
       return True
    elif strer == "No":
       return False
    else:
       pass






