from datetime import datetime
class variable:
  def __init__(self,db):
    self.db = db  
   
  def Push(self,name ,datetime, val):
    if(self.db.IfExist(name) == True):
       print("Appending")
       self.db.Insert(name,['datetime','value'],[datetime,val])
    elif(self.db.IfExist(name) == False):
       print("Creating New Data table")
       self.NewData(name)
       self.db.Insert(name,['datetime','value'],[datetime,val])

  def NewData(self,dataname):
   columnname = ['datetime','value']
   columntype = ['DATETIME UNIQUE','FLOAT']
   self.db.CreateTable(dataname,columnname , columntype)
   

  def GetPercentage(self,name,starttime,endtime):
   result  = self.db.Query("SELECT * FROM `" + name +  "` WHERE datetime BETWEEN ' " + starttime + " ' AND ' " + endtime + " ' ORDER BY `datetime` ASC")
   if(len(result) == 0):
      return None
   valuearray = []
   for i in range(len(result)):
     time,value = result[i]
     valuearray.append(value)
   openval = valuearray[0]
   closeval = valuearray[len(valuearray) - 1]
   percentage = ((closeval/openval) - 1 ) * 100
   return percentage


  def GetDB(self):
    return self.db


