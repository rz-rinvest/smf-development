import mysql.connector


class MYSQL:

  def __init__(self,dbname):
      self.db = mysql.connector.connect(  host="localhost",user="root",password="arshad956", database=dbname )


  def CreateTable(self,tablename,columnname , columntype):
      if(len(columnname) != len(columntype)):
         print("Incorrect table data")
      else:
         cur = self.db.cursor()
         tabledata = ""
         for i in range(len(columnname)):
            if(i != len(columnname) - 1):
              tabledata = tabledata + columnname[i] + " " + columntype[i] + ","
            else:
              tabledata = tabledata + columnname[i] + " " + columntype[i]
         sql = "CREATE TABLE `" + tablename + "` (" +  tabledata + ")"
         cur.execute(sql) 
         print(sql)

  def DropTable(self,tablename):
      mycursor = self.db.cursor()
      sql = "DROP TABLE " + tablename
      mycursor.execute(sql)
      return "Dropped" 
     

  def Query(self,query):
      mycursor = self.db.cursor()
      mycursor.execute(query)
      myresult = mycursor.fetchall()
      return myresult


  def Insert(self,tablename,keys,values):
     keydata  = ""
     valdata  = ""
     for i in range(len(keys)):
       if(i != len(keys) - 1):
              keydata = keydata + keys[i]+ ","
       else:
              keydata = keydata + keys[i]
     for i in range(len(values)):
       if(i != len(values) - 1):
              valdata = valdata + "'" + str(values[i]) + "',"
       else:
              valdata = valdata + "'" + str(values[i]) + "'"


     sql = "INSERT INTO `" + tablename + "` (" + keydata +  ") VALUES (" + str(valdata) + ")"
     try:
       cur = self.db.cursor()
       cur.execute(sql)
       self.db.commit()
       return cur.lastrowid
     except:
       print(sql)


  def IfExist(self,tablename):
    sql =  "show tables"
    cur = self.db.cursor()
    cur.execute(sql)
    try:
      myresult = cur.fetchall()
      for i in range(len(myresult)):
         if(tablename == myresult[i][0]):
            return True
      else:
         return False
    except:
      print("Error")
      exit()
 


  def ListData(self):
    sql =  "show tables"
    cur = self.db.cursor()
    cur.execute(sql)
    lister = []
    try:  
      myresult = cur.fetchall()
      for i in range(len(myresult)):
         lister.append(myresult[i][0])
      return lister
    except:    
      return []









