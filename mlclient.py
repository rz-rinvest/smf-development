import sys
import time
from RenzvosClient import Connector
from management import ClientObject

current_module = sys.modules[__name__]  
clt = ClientObject.Client()
clt.create("ml","Machine Learning")
conn = Connector.ct(clt,current_module)   

def ping(data):
  return {"print" : "Got Response from Company Analysis"}


def ProcessOne(data):
  print("Welcome to the Process One")
  time.sleep(1)
  print("Processing 20%")
  time.sleep(1)
  print("Processing 40%")
  time.sleep(1)
  print("Processing 60%")
  time.sleep(1)
  print("Processing 80%")
  time.sleep(1)
  print("Processing 100%")
  time.sleep(1)
  print("Process Completed")

def ProcessTwo(data):
  price = 32
  
