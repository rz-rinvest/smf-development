from RenzvosClient import Connector
from management import ClientObject

class divert():

  def new(self,name,desc):
     self.clt = ClientObject.Client()
     self.clt.create(name,desc)
     self.conn = Connector.ct(clt,__name__)
     return self.conn  
  
  def status(self,conn):
     self.conn.status
