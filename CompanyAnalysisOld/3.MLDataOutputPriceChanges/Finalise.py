import pandas as pd
import csv
import datetime
import az as stock
from datetime import date, timedelta


def ApproximateVal(ticker,pdate):
  dateObj = datetime.datetime.strptime(pdate, '%d-%m-%Y')
  if stock.GetStock(pdate,ticker) == "No Data":
    found = False
    for i in range(3):
     dateObj = dateObj - timedelta(days=1)
     pdate =  datetime.datetime.strftime(dateObj, '%d-%m-%Y')
     val = stock.GetStock(pdate,ticker)
     #print(ticker + "   " + pdate +  "  "  + str(val))
     if val != "No Data":
       found = True
       break
     else:
       found = False
  else:
    val  = stock.GetStock(pdate,ticker)
    found = True

  if found == False:
    for i in range(3):
     dateObj = dateObj + timedelta(days=1)
     pdate =  datetime.datetime.strftime(dateObj, '%d-%m-%Y')
     val = stock.GetStock(pdate,ticker)
     #print(ticker + "   " + pdate +  "  "  + sre(val))
     if val != "No Data":
       found = True
       break  
     else:
       return found
  return val  


category = "3mo"
mlp =  pd.read_csv("ML_Data/ResultLess/" + category + "/" + "mlproperties.csv")


enddate = mlp.iloc[0,1]
ticker = mlp.iloc[0,2]
ticker = ticker[:-3]


dateObj = datetime.datetime.strptime(enddate, '%d-%m-%Y')

if category == "3mo":
  dateObj = dateObj + timedelta(days=90)
elif category == "6mo":
  dateObj = dateObj + timedelta(days=180)


pdate = datetime.datetime.strftime(dateObj, '%d-%m-%Y')

start = ApproximateVal(ticker,pdate)
end = ApproximateVal(ticker,enddate)

startprice = float(start["NSE:" + ticker]['open'])
endprice = float(end["NSE:" + ticker]['open'])

pricechange = (endprice - startprice) /  startprice
print(str(pricechange))







