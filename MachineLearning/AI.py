import pandas as pd
import numpy as np
from MachineLearning import PremadeEstimator
from Console import ConsoleData
import math

def SubstituteStrings(train):
  types = AppendCheckDataTypes(train,[])
  for j in range(len(types)):
    if(types[j]["Type"] == "str"):
      colname = types[j]["Column"] 
      colno = types[j]["ColNo"]
      vals = list(dict.fromkeys(train[colname].tolist()))
      substutes = []
      for i in range(1,len(vals) + 1):
        substutes.append({"ID" : i , "Value" : vals[i-1]})
      #print(substutes)
      for i in range(len(train.index)):
        value = train.iloc[i,colno]
        for k in range(len(substutes)):
            sub = substutes[k]            
            if(value == sub["Value"]):
               train.iloc[i,colno] = np.float64(sub["ID"])
        
def SubstitueOutput(output):
   substutes = []
   print(output)
   if(output[0].__class__.__name__ == "str"):
        vals = list(dict.fromkeys(output.tolist())) 
        for i in range(1,len(vals) + 1):
           substutes.append({"ID" : i , "Value" : vals[i-1]})
        print(substutes)
        for i in range(output.size):
           value = output.at[i]
           for k in range(len(substutes)):
            sub = substutes[k]            
            if(value == sub["Value"]):
               output.at[i] = np.int64(sub["ID"])
   if(output[0].__class__.__name__ == "float64"):
     substutes = TreatFloatOutput(output)
   return substutes


def CalclateTime(features):
  cls = ConsoleData.ClsData()
  exp = cls.get("MLExponentialFactor")
  mult = cls.get("MLMultiplierFactor")
  constant = cls.get("MLAdditionalConstant")
  return math.pow((mult * features),exp) + constant
#def TreatFloatOutput(output):




def AppendCheckDataTypes(df,lister):
  for j in range (len(df.columns)):
    typec = df.iloc[0,j].__class__.__name__
    for i in range (len(df.index)):
      columntypes = []
      typer = df.iloc[i,j].__class__.__name__
      if(typec != typer):
         print("Multiple Types found in an column")
         exit()
      columntypes.append(typer)
    columntypes = list(dict.fromkeys(columntypes))
    lister.append({"Column" : df.columns[j] ,"Type" : columntypes[0] , "ColNo" : j})
  return lister

def CastToFloat64(df):
  for i in range (len(df.index)):
    for j in range (len(df.columns)):
       df.iloc[i,j] = np.float64(df.iloc[i,j])
  return df

def Serialise(df):
  try:
    for col_name in df.columns:
      df[col_name] = df[col_name].tolist()
  except:
    df = pd.DataFrame({'Output' : df.tolist()})
  return df

def DeleteRows(df,output,nonzerocols):
  rowstodelete = []
  nanframe = df.isnull()
  for i in range (len(df.index)):
    for j in range (len(df.columns)):
      if(nanframe.iloc[i,j] == True):
        #print(str(train.iloc[i,j]) + " at " + train.columns[j] + " column in " + str(i) + "row")
        rowstodelete.append(i)
  for i in range (len(nonzerocols)):
    zeros = df[nonzerocols[i]].tolist()
    for j in range(len(zeros)):
      if(zeros[i] == 0 or np.isnan(zeros[i])):
         print(zeros[i])
         rowstodelete.append(j)

  nanframe = output.isnull()
  for i in range (output.size):
    if(nanframe.iloc[i] == True):
        #print(str(train.iloc[i,j]) + " at " + train.columns[j] + " column in " + str(i) + "row")
        rowstodelete.append(i)

     
  rowstodelete = list(dict.fromkeys(rowstodelete))

  for i in range(len(rowstodelete)):  
    #print(str(rowstodelete[i] ) +  "  " + str(len(train)) )
    df = df.drop(rowstodelete[i] ,0,inplace = False)
    output = output.drop(rowstodelete[i] ,0,inplace = False)
  df.index=range(0,len(df))
  output.index=range(0,len(output))
  return df,output


def Execute(train,out,predict_x,nonzerocols):

  train,train_y  = DeleteRows(train,out.iloc[:, 0],nonzerocols)
  SubstituteStrings(train)
  resultsarray = SubstitueOutput(train_y)
  train = CastToFloat64(train)
  train = Serialise(train)
  train_y = Serialise(train_y)
  print(train)
  print(train_y)

  result,prob = PremadeEstimator.DO(train,train_y,predict_x)
  data = []
  for i in range(len(result)):
    resultid = 0
    for j in range(len(resultsarray)):
       if(resultsarray[j]["ID"] == result[i]):
         resultid = j
         break
    data.append({"Result" : resultsarray[j]["Value"] , "Probability" : prob[i]})
  return data   
    















