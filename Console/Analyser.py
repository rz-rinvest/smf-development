from datetime import *
import Variable

class Analyser:
  def __init__(self,db):
    self.var = Variable.variable(db)
 
  def MissingStocksDailyData(self,name,sdate,edate):
    lister = []
    delta = edate - sdate   
    for i in range(delta.days + 1):
      fday = sdate + timedelta(days=i)
      tday = sdate + timedelta(days=(i+1))
      if fday.weekday() == 5 or fday.weekday() == 6:
         continue
      #xpoints.append(fday.strftime("%Y-%m-%d")) 
      result = self.var.GetRange(name,fday.strftime("%Y-%m-%d"),tday.strftime("%Y-%m-%d"))
      if result == None:
        lister.append(fday)
    return lister
    


  def MissingCryptoDailyData():
    pass


