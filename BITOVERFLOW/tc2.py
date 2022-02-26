import time
from bfclient_python import Connector
from bfclient_python import bfclientobject as bfc


clt = bfc.Client()
clt.create("test2","Test Client")
conn = Connector.ct(clt,__name__)


print("Press any key to do some test communication")

input()

#print(conn.get("test1","ping",{})['print'])


print("Doing some stream testing in five seconds")

input()


conn.getstream("test1","pingstream",{},"Output")



def Output(data):
  print(data)


input()



