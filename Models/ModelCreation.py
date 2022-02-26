from Models import CaseObject
import pandas as pd

class ModelCreation:
  index = []
  ml = []
  data = []
  cases = []
  
  
  def __init__(self,index,outptfn):
     self.outputfn = outptfn
     print(outptfn)
     for i in index:
       inp,ml = i
       self.index.append(inp)
       self.ml.append(ml)

       
  def NewCase(self):
    return CaseObject.obj(self.index,self.outputfn)
  
  
  def AddCase(self,case):
    self.cases.append(case)
     
  
  def Data(self):
     data = []
     df = pd.DataFrame(data,columns=self.index)
     for i in self.cases:
       row = i.datarow()
       if(row != None):
         df.loc[len(df.index)] = row
       else:
          print("Error ROW NOT COMPLETED")
     return df
     
  def Printmodel(self):
     data = []
     mlindex = []
     
     for i in range(len(self.ml)):
        if self.ml[i] == True:
          mlindex.append(self.index[i])
          
     df = pd.DataFrame(data,columns=mlindex)
     
     for i in self.cases:
       row = i.mlrow(mlindex)
       if(row != None):
         df.loc[len(df.index)] = row
       else:
          print("Error Case ROW NOT COMPLETED")
     
           
     for case in self.cases:
       case.ParseOutput()
     
     outputarr = []
     for case in self.cases:
       outputarr.append(case.output)
     dfout = pd.DataFrame({"output" : outputarr})  
     
     return df,dfout     
        
        
        
        
        
        
        
        
