from Recorder import Queue
from Recorder import recf
import Mysql
import Variable
import time


db = Mysql.MYSQL("stocks")
var = Variable.variable(db)
q = Queue.queue(var)


q.Request("NSE:TATAMOTORS_Price","","")















while True:
  recf.screen_clear()
  data = q.DisplayData()
  for i in range(len(data)):
    ticker = data[i]['Name']
    status = data[i]['Status']
    print( ticker + " :  "  + status )
  print(q.QueueLength())
  time.sleep(1)
  pass





