#command="python3 caclient.py"
#os.system("mate-terminal -e 'bash -c \""+command+";bash\"'")



from bfserver import server



'''
@get('/ping')
def my_process():
  #req_obj = json.loads(request.body.read())
  print('ping')
  return 'pingok'


@post('/report')
def report():
  req_obj = json.loads(request.body.read())
  global reports
  reports.append(req_obj)
  status()
  return ''





@get('/ca-get-jobs')
def cajobs():
  status()
  return jobs['ca']


  
@post('/ca-update-jobs')
def jobsupdate():
  global jobs
  CA.jobsupdate(request.body.read(),jobs)
  status()
  return ""
  
  
  
@post('/ca-yf-check')
def yfcheck():
  global jobidcount
  global jobs
  jobidcount = jobidcount + 1
  return CA.yfcheck(jobs,jobidcount)
  

@get('/consoledata')
def consoledata():  
  
  return json.dumps({"jobs" : jobs , "reports" : reports })




'''












