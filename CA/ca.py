from CA.configcontrol import ConfigControl
from CA.YahooFinance import Importer
from CA.YahooFinance import Cleaner
from CA.YahooFinance import ComparingTable



class CA:
  def __init__(self):
    pass
    
 
  def Startup(self,am):
    return self.CheckForNewStocks(am)
     
     
  def CheckForNewStocks(self,am):
     #self.globalvar.ca_status = "checking for new stocks" 
     config = ConfigControl.ConfigControl()
     stocks = am.GetAllStocks()
     yfstocks = []
     for stock in stocks:
        if stock.yfverified == True and stock.yfstatus == "New":
          yfstocks.append(stock)
          
          
     a = config.val.get('Current Operation')    
     if a == 'Initiated' or a == 'Ready' :
        self.CheckYF(yfstocks,am,config)
     
     
       
     if config.val.get('Current Operation') == 'Downloaded':
       cl = Cleaner.Cleaner()
       print("Processed")
       config.val.update('Current Operation' , 'Processed')
     
     print("Creating Machine Learning DataSet")
     
     if config.val.get('Current Operation') == 'Processed':
        Ct = ComparingTable.ComparingTable()
        pr = Ct.Make("3mo")
        return pr
        
     
    
     
  def CheckYF(self,yfstocks,am,config):
     print("Checking")
     config.val.update('Current Operation' , 'Initiated')    
     if len(yfstocks) != 0:
        imp = Importer.YF_Import(yfstocks)
        result = imp.returner()
        imported  = result['Imported']
        notaval = result['NAStocks']
        
        for stock in imported:
          stock.yfstatus = "Imported"
        for stock in notaval:
          stock.yfstatus = "NA"
        
        am.Update(imported)
        am.Update(notaval)
        config.val.update('Current Operation' , 'Downloaded')
        print("Downloaded")
     
 
     
     
   
