import csv
import json 
import pandas as pd
from datetime import date, timedelta
import datetime
import yahoo_fin.stock_info as si



def AppendTickerValues(mainjson, date , ticker_name , openp , high , low , closep , volume ):
  if date == "" or date  == None or date == "Nan":
    return 0
 
  dateindex = Indexof(mainjson,date,False) 
  datedetails = mainjson[dateindex].get(date)
  tickerIndex = Indexof(datedetails,ticker_name,False)
  if tickerIndex == "Error":
    ticker = {}
    ticker['open'] = openp
    ticker['high']  = high
    ticker['low'] = low
    ticker['close'] = closep
    ticker['volume'] = volume
    add = { ticker_name :  ticker}
    a = mainjson[dateindex].get(date).append(add)
    return "Added"
  else:
    return "Skipped"
    pass
  
  

def Indexof(mainjson,date,debug):
  for i in range(len(mainjson)):
    element = mainjson[i]
    el_val = list(mainjson[i].keys())[0]
    if debug:
      print("Checking " + el_val + " for " + date)
    if el_val == date:
      if debug:
        print("Found " + el_val + " as " + date)
      return i
      break
  else:
    return "Error"

def GetStock(inputdate,ticker):
  dateraw = str(inputdate)
  dateobj = datetime.datetime.strptime(dateraw, '%d-%m-%Y')
  year = datetime.datetime.strftime(dateobj,'%Y')
  try:
    f = open("splitted/" + year + '.json') 
  except:
    return "No Year File"
  data = json.load(f)
  index = Indexof(data,inputdate,False)
  ticker = "NSE:" + ticker
  datefile = data[Indexof(data,inputdate,False)][inputdate]
  index = Indexof(datefile,ticker,False)
  if index == "Error":
    return "No Data"
  else:
    return datefile[index]


def PutStock(date,ticker,opener,high,low,closer,volume):
  val = GetStock(date,ticker)
  if val == "No Data":
    dateobj = datetime.datetime.strptime(date, '%d-%m-%Y')
    year = datetime.datetime.strftime(dateobj,'%Y')
    f = open('splitted/' + str(year) + '.json') 
    data = json.load(f)
    ticker = "NSE:" + ticker
    print("Date : " + date + " " + ticker + " " + str(opener) +  " " + str(high)  + " " + str(low)  + " " + str(closer)  + " " + str(volume))
    AppendTickerValues(data, date , ticker , opener , high , low , closer , volume )
    json_object = json.dumps(data, indent = 4) 
    with open("splitted/" + str(year) + ".json", "w") as outfile: 
      outfile.write(json_object) 
    return "Adding"
  elif val == "No Year File":
    print(" No Year File")
    return "Creating Year File"
  else:
    return "Data Exist"



#print(PutStock("03-09-2005","TATASTEEL",16,65,65,56,23))
#print(GetStock("05-03-2021","TATASTEEL"))

def Bulkadd(data):
  ydata = {} 
  count = 0
  for year in range(2005,2022):
    print("Loading " + str(year))
    f = open('splitted/' + str(year) + '.json') 
    ydata[str(year)] = json.load(f)
  
  addcount = 0
  skipcount = 0

  for i in range(len(data)):
    date = data[i]['date']
    ticker = data[i]['ticker']
    opener = data[i]['open']
    high = data[i]['high']
    low = data[i]['low']
    closer = data[i]['close']
    volume = data[i]['volume']
    dateobj = datetime.datetime.strptime(date, '%d-%m-%Y')
    year = datetime.datetime.strftime(dateobj,'%Y')
    ticker = "NSE:" + ticker
    ret = AppendTickerValues(ydata[year], date , ticker , opener , high , low , closer , volume )
    if ret == "Added":
     addcount = addcount + 1  
     print("Added " + str(addcount) + " elements and skipped " + str(skipcount) + " elements , Now adding" + ticker + " on " + date)
    elif ret == "Skipped":
     skipcount = skipcount + 1
     print("Added " + str(addcount) + " elements and skipped " + str(skipcount) + " elements , Now adding" + ticker + " on " + date)
  for year in range(2005,2022):
    print("Saving " + str(year))
    json_object = json.dumps(ydata[str(year)], indent = 4) 
    with open("splitted/" + str(year) + ".json", "w") as outfile: 
     outfile.write(json_object) 



def CheckLatest(output,ticker):

  today = date.today()
  checkdate =  datetime.datetime.strftime(today, '%d-%m-%Y')
  

  while GetStock(checkdate,ticker) == "No Data":
   today = today - timedelta(days=1)
   checkdate =  datetime.datetime.strftime(today, '%d-%m-%Y')
  
  today = today + timedelta(days=1)
  checkdate =  datetime.datetime.strftime(today, '%d-%m-%Y')
  startdate = checkdate
  
  startObj =  datetime.datetime.strptime(startdate, '%d-%m-%Y')
  ystart = datetime.datetime.strftime(startObj, '%m/%d/%Y')
  try:
    df = si.get_data(ticker + ".NS" , start_date = ystart)
    for dateind in range(len(df)):
      idate = df.index[dateind]
      datestr = datetime.datetime.strftime(idate,"%d-%m-%Y")
      opener = float(df.iloc[dateind,0])
      high  = float(df.iloc[dateind,1])
      low  = float(df.iloc[dateind,2])
      closer = float(df.iloc[dateind,3])
      volume = float(df.iloc[dateind,5])
      add = { 'ticker' : ticker , 'date' : datestr , 'open' : opener , 'high' : high , 'low' : low , 'close' : closer , 'volume' : volume }
      output.append(add)
  except:
      print("Getting prices error")
  
  

def Update():
  tickers = pd.read_csv("tickers.csv")
  output = []
  for i in range(10):
    ticker = tickers.iloc[i,0]
    print("Updating " + ticker)
    CheckLatest(output,ticker)
  Bulkadd(output)





'''

def Analyz():
tickers = pd.read_csv("tickers.csv")
year = '2005'
f = open("splitted/" + year + '.json') 
data = json.load(f)

i=0
key = data[0].keys()
datefile = data[0][list(data[0].keys())[0]]
for i in range(len(tickers)):
  ticker = tickers.iloc[i,0]
  ticker = "NSE:" + ticker
  index = Indexof(datefile,ticker)
  if index == "Error":
    print(ticker + " not found")


'''








