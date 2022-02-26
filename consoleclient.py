import sys
import time
from RenzvosClient import Connector
from management import ClientObject


clt = ClientObject.Client()
clt.create("console","Console")
conn = Connector.ct(clt,__name__)   


time.sleep(2)

print(conn.get("ceo","ping",{})['print'])

time.sleep(2)


'''
print(conn.get("ml","ping",{})['print'])

time.sleep(2)

print(conn.get("var","ping",{})['print'])

time.sleep(2)

print(conn.get("recorder","ping",{})['print'])


time.sleep(2)
'''

conn.getstream("ca","addstockstoca",{},"Output")


def Output(data):
  print("Welcome to the Output")
  print("Your data is ")
  print(data)






input()










