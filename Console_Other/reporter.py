import json
import http.client


class reporter:

  def __init__(self, jobid):
    self.jobid = jobid
    self.conn = http.client.HTTPConnection('localhost', 8080)
    
  def success(self,message):
    self.post("report" ,json.dumps({"id" : self.jobid ,"type" : "success","message" : message} ))
  
  def warning(self,message):
    self.post("report" ,json.dumps({"id" : self.jobid ,"type" : "warning","message" : message} ))
  
  def error(self,message):
    self.post("report" ,json.dumps({"id" : self.jobid ,"type" : "error","message" : message} ))
  
  def text(self,message):
    self.post("report" ,json.dumps({"id" : self.jobid ,"type" : "text","message" : message} ))
  
  
  
  
  def post(self,name,data):
    self.conn.request('POST', '/' + name, data)
    doc = self.conn.getresponse().read()
    return doc.decode("utf-8")
    
