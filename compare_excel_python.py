# import pandas lib as pd
import pandas as pd
import datetime as dt

tenantexcel = '/Users/senthu/Downloads/frntapis.xlsx'
cmexcel = '//Users//senthu//Downloads//frntstg-ITRv1.xlsx'
gateway = 'frntstg-pvt'
firstname = 'Ming Howe'
comments = 'To add Ming Howe as API Owner'

# create empty lists for guid
guidlist = []

# get the current date and time
now = dt.datetime.now()

# read by default 1st sheet of an Excel file
df1 = pd.read_excel(tenantexcel)

# read by default 2nd sheet of an Excel file
df2 = pd.read_excel(cmexcel)

# filter by GW,Username and api name and write guid to Excel sheet
for i in df1.index:
    if df1['gateway'][i] == gateway and df1['first_name'][i] == firstname and df1['Comments'][i] == comments:
        for j in df2.index:
            if df1['api_name'][i] == df2['title2'][j]:
                guidlist.append([df2['guid'][j], df2['title2'][j], df1['gateway'][i], df1['first_name'][i]])
                break

# create dataframe from your guidlist
df = pd.DataFrame(list(guidlist), columns=['GUID', 'API Name', 'Gateway', 'User Name'])

# get your desired output
df.to_excel('//Users//senthu//Downloads//FRNTFINAL//' + firstname + '_' + gateway + '_' + str(now) + '.xlsx')
print(df)