from Assets import AssetManager
import Variable
import Mysql
from datetime import *
import matplotlib.pyplot as plt
from Analyser import Analyser


db = Mysql.MYSQL("stocks")


assets = AssetManager.AM()
anal = Analyser.Analyser(db)


sdate = date(2005, 1, 15)   # start date
edate = date(2015, 1, 15)   # end date

ex = "NSE"
name = "TATAMOTORS"
var = "Price"

print(anal.MissingDailyData(ex,name,var,sdate,edate))











