import http.client
c = http.client.HTTPConnection('localhost', 8080)


def Send(name,data):
  c.request('POST', '/' + name, data)
  doc = c.getresponse().read()
  return doc.decode("utf-8")



try:
  if Send("ping","{}") == "pingok":
    #Runing
  else:
    #Not Running
except:
  #Not Running
  
    
  


