# importing libraries
import pandas as pd
import numpy as np
import datetime as dt
#import openpyxl

sqloutput='/Users/jd/Downloads/sql.csv'
mongoout='/Users/jd/Downloads/mongo.csv'


# Read the two excel files into pandas dataframes
df1 = pd.read_csv(mongoout)
df2 = pd.read_csv(sqloutput)

# create empty lists for guid
guidlist = []

# get the current date and time
now = dt.datetime.now()


# filter by GW,Username and api name and write guid to Excel sheet
for s in df1.index:
    #if df1['svcid'][s]
        for j in df2.index:
            if df1['svcid'][s] == df2['PRODSVC'][j]:
                guidlist.append([df1['tenant'][s], df2['NAME'][j], df1['statuscode'][s], df1['count'][s]])


# create dataframe from your guidlist
df = pd.DataFrame(list(guidlist), columns=['tenant', 'API Name', 'statuscode', 'count'])


# get your desired output
df.to_excel('/Users/jd/Downloads/APIOUTPUTLIST' + str(now) + '.xlsx')
print(df)

#Test123