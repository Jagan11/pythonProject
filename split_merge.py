### setting python env varisbles
#!usr/bin/env python3

#Importing libraries
import pandas as pd
import datetime as dt
import numpy as np

#file location from mongo raw & Mysqlraw
mysqlraw = '/Users/jd/Downloads/APIIDv1.xlsx'
mongoraw = '/Users/jd/Downloads/17-02-2023_11-45-17_report.csv'

#file location from sql & mongo
#mysqloutput='/Users/jd/Downloads/sql.csv'
#mongooutput='/Users/jd/Downloads/mongo.csv'

# create empty list
guidlist_mysqlraw = []
guidlist = []

# get the current date and time
now = dt.datetime.now()

# read by default 1st sheet of an Excel file   # read by default 2nd sheet of an Excel file
df1 = pd.read_csv(mongoraw)
df2 = pd.read_excel(mysqlraw)

# remove special charaters form all colums
df1['serviceid'] = df1['serviceid'].str.replace('\W', '', regex=True)
df1['tenant'] = df1['tenant'].str.replace('\W', '', regex=True)
df1['statuscode'] = df1['statuscode'].str.replace('\W', '', regex=True)


# remove starting characters from a columns
df1['tenant'] = df1['tenant'].str[15:]
df1['statuscode'] = df1['statuscode'].str[10:]

# split a column by using a key word
df1[['count', 'svcid']] = df1["serviceid"].apply(lambda x: pd.Series(str(x).split("serviceId")))

# drop a column
dfm = df1.drop(columns=['serviceid'])


#Defining searching
searchkey = 'NULL'

# filter by GW,Username and api name and write guid to Excel sheet
for i in df2.index:
    if df2['PRODSVC'][i] != searchkey:
        guidlist_mysqlraw.append([df2['APIID'][i], df2['NAME'][i], df2['DESCRIPTION'][i], df2['PRODSVC'][i]])

# create dataframe from your guidlist
dfs = pd.DataFrame(list(guidlist_mysqlraw), columns=['APIID', 'NAME', 'DESCRIPTION', 'PRODSVC'])

# Drop empty raws from so
dfs.dropna(subset=['PRODSVC'], inplace=True)

print(df2)

# filter by GW,Username and api name and write guid to Excel sheet
for s in dfm.index:
    for j in dfs.index:
       if dfm['svcid'][s] == dfs['PRODSVC'][j]:
            guidlist.append([dfm['tenant'][s], dfs['NAME'][j], dfm['statuscode'][s], dfm['count'][s]])
            break

# create dataframe from your guidlist
df = pd.DataFrame(list(guidlist), columns=['tenant', 'API Name', 'statuscode', 'count'])


# get your desired output
df.to_csv('/Users/jd/Downloads/' + str(now) + '.csv')
print(df)


# get your desired output
#dfs.to_excel('/Users/jd/Downloads/APIOUTPUTLIST' + str(now) + '.xlsx')
#print(dfs)