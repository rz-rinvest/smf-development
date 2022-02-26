import pandas as pd

def Prep():
   index = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age' ,'SibSp','Parch','Ticket','Fare' ,'Cabin', 'Embarked']
   nonzerocols = []
   train = pd.read_csv("ExampleDataSets/train.csv", names=index, header=0)
   train.drop('PassengerId',axis='columns', inplace=True)
   train.drop('Name',axis='columns', inplace=True)
   train.drop('Cabin',axis='columns', inplace=True)
   train.drop('Fare',axis='columns', inplace=True)
   train.drop('Embarked',axis='columns', inplace=True)
   train.drop('Ticket',axis='columns', inplace=True)
   somearray = []
   val = 0
   for i in range(len(train.index)):
     somearray.append(val)
     if(val == 0):
       val = 1
     else:
       val = 0

   train['Some'] = somearray

   for i in range(len(train.index)):
      value = train.iloc[i,0]      
      if(value == 0):
         train.iloc[i,0] = "Dead"
      elif(value == 1):
         train.iloc[i,0] = "Alive"



   out = train['Survived']
   train_y = pd.DataFrame({"Output" : out})
   train.drop('Survived',axis='columns', inplace=True)
   
   return train, train_y



def Data0():
  train , train_y = Prep()
  train.drop('Sex',axis='columns', inplace=True)
  train.drop('Age',axis='columns', inplace=True)
  train.drop('SibSp',axis='columns', inplace=True)
  train.drop('Parch',axis='columns', inplace=True)
  train.drop('Some',axis='columns', inplace=True)
  predict_x = { 'Pclass' : [3, 3, 2 , 3 , 3 , 3],}
  train = train.iloc[:1]
  train_y = train_y.iloc[:1]
  nonzerocols = []
  return train,train_y,predict_x,nonzerocols

def Data1():
  train , train_y = Prep()
  train.drop('Age',axis='columns', inplace=True)
  train.drop('SibSp',axis='columns', inplace=True)
  train.drop('Parch',axis='columns', inplace=True)
  train.drop('Some',axis='columns', inplace=True)
  predict_x = { 'Pclass' : [3, 3, 2 , 3 , 3 , 3],'Sex': [1, 2 , 1 , 1 , 2 , 1]}
  train = train.iloc[:1]
  train_y = train_y.iloc[:1]
  nonzerocols = []
  return train,train_y,predict_x,nonzerocols
def Data2():
  train , train_y = Prep()
  train.drop('SibSp',axis='columns', inplace=True)
  train.drop('Parch',axis='columns', inplace=True)
  train.drop('Some',axis='columns', inplace=True)
  predict_x = { 'Pclass' : [3, 3, 2 , 3 , 3 , 3],'Sex': [1, 2 , 1 , 1 , 2 , 1],'Age': [34.5, 47, 62, 27, 22 , 14]}
  train = train.iloc[:1]
  train_y = train_y.iloc[:1]
  nonzerocols = []
  return train,train_y,predict_x,nonzerocols
def Data3():
  train , train_y = Prep()
  train.drop('Parch',axis='columns', inplace=True)
  train.drop('Some',axis='columns', inplace=True)
  predict_x = { 'Pclass' : [3, 3, 2 , 3 , 3 , 3],'Sex': [1, 2 , 1 , 1 , 2 , 1],'Age': [34.5, 47, 62, 27, 22 , 14],'SibSp': [0, 1, 0,0,1,0]}
  train = train.iloc[:1]
  train_y = train_y.iloc[:1]
  nonzerocols = []
  return train,train_y,predict_x,nonzerocols

def Data4():
  train , train_y = Prep()
  train.drop('Some',axis='columns', inplace=True)
  predict_x = { 'Pclass' : [3, 3, 2 , 3 , 3 , 3],'Sex': [1, 2 , 1 , 1 , 2 , 1],
                   'Age': [34.5, 47, 62, 27, 22 , 14],'SibSp': [0, 1, 0,0,1,0],
                     'Parch': [0,0,0,0,1,0] }
  train = train.iloc[:1]
  train_y = train_y.iloc[:1]
  nonzerocols = []
  return train,train_y,predict_x,nonzerocols

def Data5():
  train , train_y = Prep()
  predict_x = { 'Pclass' : [3, 3, 2 , 3 , 3 , 3],   'Sex': [1, 2 , 1 , 1 , 2 , 1],
               'Age': [34.5, 47, 62, 27, 22 , 14],'SibSp': [0, 1, 0,0,1,0],
                 'Parch': [0,0,0,0,1,0] ,'Some' : [0,1,0,1,0, 1]}
  train = train.iloc[:1]
  train_y = train_y.iloc[:1]
  nonzerocols = []
  return train,train_y,predict_x,nonzerocols






