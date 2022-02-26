from os import listdir
import datetime
import os
import Process as smf
from os.path import isfile, join
import pandas as pd

path = "raw"
files = [f for f in listdir(path) if isfile(join(path, f))]
six_mo = []

for i in range(len(files)):
    filename = os.path.splitext(files[i])[0]
    six_mo.append(datetime.datetime.strptime(filename, '%d-%m-%Y'))

six_mo.sort()

three_mo = []
hiddenval = 25.98







for i in range (len(six_mo)):
    if six_mo[i].month == 3 or six_mo[i].month == 9:
        three_mo.append(six_mo[i]) 


tfile = []
xfile = []

for i in range(len(three_mo)):
        tfile.append(three_mo[i].strftime('%d-%m-%Y')) 

for i in range(len(six_mo)):
        xfile.append(six_mo[i].strftime('%d-%m-%Y'))


print(tfile[-1])
print(xfile[-1])

tfile.pop()
xfile.pop()



print("3 months data veno atho 6 months data veno(Type 3 or 6)")
choice = int(input())
print("Enter Row-Coulmn Ratio in 1-100 (default is 20) :")
pn = float(input())

indexdf = pd.read_csv("rawindex" + ".csv")
ind = indexdf['index'].tolist()



if(choice == 3):  
    smf.main(xfile,ind,"3mo",pn)
elif(choice == 6):
    smf.main(tfile,ind,"6mo",pn) 
    










