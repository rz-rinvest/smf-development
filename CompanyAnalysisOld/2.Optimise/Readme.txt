Run.py starts the optimiser 

It starts the functions given in Process

Run basically divides the data into two 

3 months and 6 months data

it asks for a percentage to delete the rows and column

we find the best percentage by trial and error method

the present data is 

Percentage on col 3mo = 90.75
6MP = 91.5

and After making all the Clean Data it compares each and every two file to find THE CHANGE HAPPEND to each value
-- it takes the common intersection tickers 
-- and find the change while an extra file is created called MLproperties which contains
----start date of a row
----end date of a row
----and which stock it is


and makes an ML model and it is saved in ML_DataResultLess 
because there is one job left ... finding the price change occured when there is a change in the company values



Input 

--3 month or 6 month
--rawindex.csv
--rawfolder with all raw data
--percentage optimiser for 3 mo and 6 mo

Output
--Process folder which has 3mo and 6 mo data with no zero values and reduced to be usefull
--MLData ResultLess Folder which has ML input only
--MLProperties.csv file which has 'startdate','enddate','stockname' of the input ..to find the output


