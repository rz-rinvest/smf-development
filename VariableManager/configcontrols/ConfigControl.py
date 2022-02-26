import pandas as pd
from VariableManager.configcontrols import database
from VariableManager.configcontrols import frequency
from VariableManager.configcontrols import lastdata
from VariableManager.configcontrols import lastdatetime
from VariableManager.configcontrols import startdatetime
from VariableManager.configcontrols import status

class ConfigControl:

  def __init__(self):
    try:
      config = pd.read_csv('VariableManager/config.csv')
    except:
      dicter = {'Variable Name' : [] , 'Database' : [] , 'Frequency' : [] , 'Start-Datetime' : [] , 'Last-Datetime' : [] , 'Last_data' : [] , 'Status' : []  }
      config = pd.DataFrame(dicter)
      config.to_csv('VariableManager/config.csv' ,index=False)
    self.Functions()
 

  def new(self,name,database,fq,sdt,ldt,ld,s):
    config = pd.read_csv('VariableManager/config.csv')
    config.loc[len(config.index)] = [name,database,fq,sdt,ldt,ld,s]
    config.to_csv('VariableManager/config.csv',index=False)


  def display(self):
    print(pd.read_csv('VariableManager/config.csv'))


  def Functions(self):
    self.db = database.database()
    self.fq = frequency.frequency()
    self.ld = lastdata.last_data()
    self.ldt = lastdatetime.last_datetime()
    self.sdt= startdatetime.start_datetime()
    self.stats = status.status()
    
    
    
    
    
    
    
    
    
    
    
    
