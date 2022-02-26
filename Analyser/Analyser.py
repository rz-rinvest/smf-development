from datetime import *

class Analyser:

  def __init__(self,db):
    import Variable
    from Assets.Exchanges import exchange
    self.var = Variable.variable(db)
    self.ex = exchange.Exchanges()
 
  def MissingDailyData(self,exchange,name,var,sdate,edate):
    lister = []
    opentime,closetime,weekdays = self.ex.GetDetails(exchange)
    ot = datetime.strptime(opentime, '%H:%M:%S')
    ot = time(ot.hour,ot.minute,ot.second)
    ct = datetime.strptime(closetime, '%H:%M:%S')
    ct = time(ct.hour , ct.minute ,  ct.second)

    varname = exchange + ":" + name + "_" + var   
    delta = edate - sdate

    for i in range(delta.days + 1):
      fday = sdate + timedelta(days=i)
      tday = sdate + timedelta(days=(i+1))
      fday = datetime.combine(fday,ot)
      weekday = str(fday.weekday())
      wds = set(weekdays)
      if weekday not in wds:
         continue
 
      opencl = fday.strftime('%Y-%m-%d %H:%M:%S')
      value = self.var.GetOne( varname , opencl )
      if value == None:
         lister.append(fday)

    return lister


      





