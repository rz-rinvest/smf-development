import json
import Variable
import datetime
import Mysql
from datetime import datetime

ydata = {} 


db = Mysql.MYSQL("stocks")
var = Variable.variable(db)

for year in range(2016,2017):
    print("Loading " + str(year))
    f = open('splitted/' + str(year) + '.json') 
    ydata[str(year)] = json.load(f)


for year in range(2016,2017):
  days = ydata[str(year)]
  for i in range(120,len(days)):
    day = days[i]
    date = list(day.keys())[0]
    info = day[str(date)]
    for j in range(len(info)):
      stockname = list(info[j].keys())[0]
      details = info[j][str(stockname)]
      popen = details['open']
      pclose = details['close']
      vol = details['volume']
      datetimeobject = datetime.strptime(date,'%d-%m-%Y')
      datein = datetimeobject.strftime('%Y-%m-%d')
      opendate = datein + " 09:00:00"
      closedate = datein + " 15:00:00"
      print ("Day" + opendate + " Stock: " + stockname + " O : " + str(popen) )
      print ("Day" + closedate + " Stock: " + stockname + " C : " + str(pclose) )
      var.Push(stockname + "_Price", opendate , popen )
      var.Push(stockname + "_Price", closedate , pclose )
      var.Push(stockname + "_Vol" , closedate , vol )
















