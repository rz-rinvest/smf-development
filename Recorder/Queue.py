import Variable
from threading import Thread
import time


class queue:

  data = []
  que = []
  
  

  def __init__(self,variable):
      self.var  = variable
      db = variable.GetDB()
      varb = db.ListData()
      for i in range(len(varb)):
         ticker = {"Name" : varb[i] , "Status" : "Not Active"}
         self.data.append(ticker) 
      
      t = Thread(target = self.Listener) 
      t.setDaemon(True)
      t.start()
      self.lasttime = time.time()

      

  def Request(self,name ,datetime, val):
     i = self.FindIndex(name)
     if(self.data[i]['Status'] != "Busy"):
                self.data[i]['Status'] = "Busy"
                self.que.append({"Name" : name , "Datetime" : datetime , "Value" : val , "Index" : i})
                
     
    

  def DisplayData(self):
    Ddata = []
    for i in range(len(self.data)):
       if(self.data[i]['Status'] != "Not Active"):
           Ddata.append(self.data[i])
    return Ddata

  def Listener(self):
    while True:
      if(len(self.que) > 0):
         obj = self.que[0]
         #d
         i = obj['Index']
         self.data[i]['Status'] = "Active"
         self.que.pop(0)


  def FindIndex(self,name):
    for i in range(len(self.data)):
        if(self.data[i]['Name'] == name):
            return i


  def QueueLength(self):
    return len(self.que)








