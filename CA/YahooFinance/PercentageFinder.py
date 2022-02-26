import time
import math

class PercentageFinder:


      
    def PreparePcs(self,graphcount,ul,ll):
        graphconfig = [15,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        gc = graphconfig[graphcount - 1]
        pcs = []
        space = ul - ll
        print("Graphcount " + str(graphcount))
        for i in range(gc):
            pl = ll + (space/gc * i)
            pu = ll + (space/gc * (i+1))
            mp = (pu+pl)/2
            pcs.append({'ll': pl , 'ul' :  pu ,'mp' : mp})
        return pcs
            
    
    
        
        
      
    def Plot(self,classer,ul,ll,loopcount,graphcount,finallist):
        pcs = self.PreparePcs(graphcount,ul,ll)
      
        points = []  
        for i in range(len(pcs)):
          points.append(pcs[i]['mp'])
        
        quantity = []
        
        for i in range(len(points)):
          loopcount = loopcount + 1 
          data = classer.demo(classer.curfiles,classer.index,points[i])
          print({"loopcount" : loopcount , "percentage" : points[i] ,"quantity" : data})
          quantity.append(data)
        
        
        
        max_value = max(quantity)
        max_index = quantity.index(max_value)
        
        min_value = min(quantity)
        min_index = quantity.index(min_value)
        
        
        
        
        middle_value = (max_value+min_value) / 2
        
        indexabove = []
        for i in range(len(quantity)):
          if(quantity[i] > middle_value):
            indexabove.append(i)
        
        getout = False
        if len(indexabove) == 0:
          print("Exiting because no value above half")
          getout = True 
        
        u = max([abs(points[max_index]),abs(points[max_index - 1])])
        l = min([abs(points[max_index]),abs(points[max_index - 1])])
    
        if (u  - l  <= 0.5):
          print("Exiting because difference between " + str(u) + " and " + str(l) + " is very less")
          getout = True   
          
        finallist.append({"percentage" : points[max_index] , "quantity" : max_value})
        if(getout == False):
          
        
          nll = pcs[indexabove[0]]['ll']
          nul = pcs[indexabove[len(indexabove) - 1]]['ul']
        
     
          
          
          rescursivecatcher = self.Plot(classer,nul,nll,loopcount,graphcount+1,finallist)
          return rescursivecatcher
        else:
          ind = 0
          for i in range(len(finallist)):
            if(finallist[i]['quantity'] > finallist[ind]['quantity']):
              ind = i
          return finallist[ind]
        
    
    
    
    
    
    
        
