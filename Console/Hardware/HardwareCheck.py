import pandas as pd
from MachineLearning import AI
from Console.Hardware import HardwareCheckF
import time
from Console import ConsoleData
print("Testing your hardware benchmarks")

train, train_y , predict_x , nonzerocols  = HardwareCheckF.Data0()
starttime = time.time()
AI.Execute(train, train_y,predict_x,nonzerocols)
onetime = time.time() - starttime

train, train_y , predict_x , nonzerocols  = HardwareCheckF.Data1()
starttime = time.time()
AI.Execute(train, train_y,predict_x,nonzerocols)
twotime = time.time() - starttime

train, train_y , predict_x , nonzerocols  = HardwareCheckF.Data2()
starttime = time.time()
AI.Execute(train, train_y,predict_x,nonzerocols)
threetime = time.time() - starttime

train, train_y , predict_x , nonzerocols  = HardwareCheckF.Data3()
starttime = time.time()
AI.Execute(train, train_y,predict_x,nonzerocols)
fourtime = time.time() - starttime

train, train_y , predict_x , nonzerocols  = HardwareCheckF.Data4()
starttime = time.time()
AI.Execute(train, train_y,predict_x,nonzerocols)
fivetime = time.time() - starttime

train, train_y , predict_x , nonzerocols  = HardwareCheckF.Data5()
starttime = time.time()
AI.Execute(train, train_y,predict_x,nonzerocols)
sixtime = time.time() - starttime

choice = 'Y'

while (choice == 'Y'):

  calcone = AI.CalclateTime(1)
  calctwo = AI.CalclateTime(2)
  calcthree = AI.CalclateTime(3)
  calcfour = AI.CalclateTime(4)
  calcfive = AI.CalclateTime(5)
  calcsix = AI.CalclateTime(6)

  dicter = { "Features"  : [1,2,3,4,5,6] , 
            "Time Taken" : [onetime,twotime,threetime,fourtime,fivetime,sixtime] , 
            "Calculated Time" : [calcone,calctwo,calcthree,calcfour,calcfive,calcsix]}
  df = pd.DataFrame(dicter)
  print("Your benchmark results are")
  print(df)

  print("Do you want to update your Hardware Variables (Y/N) ")
  cls = ConsoleData.ClsData()
  choice = str(input())

  if(choice == "Y"):
    print("Please Enter your Exponential Factor")
    cls.update("MLExponentialFactor",float(input()))
    print("Please Enter your Linear Factor") 
    cls.update("MLMultiplierFactor",float(input()))
    print("Please Enter you additional constant")
    cls.update("MLAdditionalConstant",float(input()))
















