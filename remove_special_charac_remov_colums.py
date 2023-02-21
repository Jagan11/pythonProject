# import pandas lib as pd
import pandas as pd
import datetime as dt

apiids = '//Users//senthu//OneDrive - GovTech//Desktop//Mongo Export Task//APIIDv1.xlsx'
cmexcel = '//Users//senthu//OneDrive - GovTech//Desktop//Mongo Export Task//17-02-2023_11-45-17_report.csv'

# create empty lists for guid
guidlist = []

# get the current date and time
now = dt.datetime.now()

# read by default 1st sheet of an Excel file
df1 = pd.read_csv(cmexcel)

# read by default 2nd sheet of an Excel file
df2 = pd.read_excel(apiids)

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
dff = df1.drop(columns=['serviceid'])

# get your desired output
dff.to_excel('//Users//senthu//OneDrive - GovTech//Desktop//Mongo Export Task//' + str(now) + '.xlsx')
print(dff)