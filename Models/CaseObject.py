from VariableManager import Functions

class obj:

  def __init__(self,index,outputfn):
     self.inputs = index
     self.values = []
     self.outputfn = outputfn
     self.output = None
     for i in index:  
       self.values.append(None)
      
  
  def Set(self,name,val):
     for i in range(len(self.inputs)):
       if self.inputs[i] == name:
          self.values[i] = val   
  
  def Get(self,name):
     for i in range(len(self.inputs)):
        if self.inputs[i] == name:
           return self.values[i]
           
  
  
  def mlrow(self,mlindex):
     

     output = []
     
     for name in mlindex:
       value = self.Get(name)
       output.append(value)
     
     for i in range(len(output)):
       if output[i] == None:
          return None
     else:
       return output        
  
  def datarow(self):
     return self.values
  
  
  def ParseOutput(self):
    self.output = Functions.get(self.outputfn,self)
     
     
     
     
     
  
