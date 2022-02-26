import http.client
import os
import sys
import time
import json
from Console_Other import reporter
from RenzvosClient import Connector
from management import ClientObject

current_module = sys.modules[__name__]  
clt = ClientObject.Client()
clt.create("ca","Company Analysis")
conn = Connector.ct(clt,current_module)   



def addstockstoca(data,stream):
   
   report.success('test')
   report.warning('abcde')




a = input()

'''

am = AssetManager.AM()
sca = ca.CA()
a,b = sca.Startup(am)
st.write(a)
st.write(b)

'''





