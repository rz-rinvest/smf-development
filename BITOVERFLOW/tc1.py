import time
from bfclient_python import Connector
from bfclient_python import bfclientobject as bfc


clt = bfc.Client()
clt.create("test1","Test Client")
conn = Connector.ct(clt,__name__)




def ping(data):
  print("Got a ping")
  return {"print" : "Hello from the other side"}



def pingstream(data,stream):
  
  print("Welcome to the Process One")
  #stream.push({"print" : "This"})
  time.sleep(1)
  print("Processing 20%")
  #stream.push({"print" : "is"})
  time.sleep(1)
  print("Processing 40%")
  #stream.push({"print" : "a"})
  time.sleep(1)
  print("Processing 60%")
  #stream.push({"print" : "ping"})
  time.sleep(1)
  print("Processing 80%")
  #stream.push({"print" : "from"})
  time.sleep(1)
  print("Processing 100%")
  #stream.push({"print" : "other"})
  time.sleep(1)
  print("Process Completed")
  #stream.push({"print" : "side"})
  

def ProcessTwo(data):
  price = 32
  

a = input()




