import json
import Variable
import datetime
import Mysql
from datetime import datetime

ydata = {} 


db = Mysql.MYSQL()

for year in range(2008,2022):
    print("Loading " + str(year))
    f = open('splitted/' + str(year) + '.json') 
    ydata[str(year)] = json.load(f)


for year in range(2008,2022):
  days = ydata[str(year)]
  for i in range(len(days)):
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
      Variable.Push(db,stockname + "_Price", opendate , popen )
      Variable.Push(db,stockname + "_Price", closedate , pclose )
      Variable.Push(db,stockname + "_Vol" , closedate , vol )
















