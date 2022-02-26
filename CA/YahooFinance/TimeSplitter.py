from os import listdir
import datetime
import os
from os.path import isfile, join
import pandas as pd

path = "CA/YahooFinance/storage/values"
files = [f for f in listdir(path) if isfile(join(path, f))]
six_mo = []

for i in range(len(files)):
    filename = os.path.splitext(files[i])[0]
    six_mo.append(datetime.datetime.strptime(filename, '%d-%m-%Y'))

six_mo.sort()
three_mo = []
for i in range (len(six_mo)):
    if six_mo[i].month == 3 or six_mo[i].month == 9:
        three_mo.append(six_mo[i]) 


tfile = []
xfile = []

for i in range(len(three_mo)):
        tfile.append(three_mo[i].strftime('%d-%m-%Y')) 

for i in range(len(six_mo)):
        xfile.append(six_mo[i].strftime('%d-%m-%Y'))


tfile.pop()
xfile.pop()



indexdf = pd.read_csv("CA/YahooFinance/storage/rawindex" + ".csv")
ind = indexdf['index'].tolist()



def Threemonthfiles():
    return xfile



def Sixmonthfiles():
    return tfile


def rawindex():
    return ind
    
def NextPeriod(name,months):
   inpobj = datetime.datetime.strptime(name, '%d-%m-%Y')
   nextdate = inpobj + relativedelta(months=+6)
   return nextdate.strftime("%Y-%m-%d %H:%M:%S")







