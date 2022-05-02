print("############################################################")
print("################## STEP 0 - DATA LOADING ###################")
print("############################################################")

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns 

sns.set()

df = pd.read_csv('data.csv',encoding="ISO-8859-1", dtype={'InvoiceNo': str,'CustomerID': str,'StockCode': str})

print(len(df), "records were read from file.")

print("\n############################################################")
print("################## STEP 1 - DATA CLEANING ##################")
print("############################################################")

df_headers = df.head()

df.info()
df['InvoiceDate'] = pd.to_datetime(df.InvoiceDate, format='%m/%d/%Y %H:%M')

print(df_headers)

"############### DROP NULL VALUES ###############"

df_cl = df.dropna()
df_cl.isnull().sum().sort_values(ascending=False)

df_cl.info()

"############### DROP Neg. QUANTITY VALUES ###############"

df_cl = df_cl[df_cl.Quantity > 0]

print(len(df_cl), "records left after dropping null values from certain columns.")


print("\n############################################################")
print("################## STEP 2 - DATA ENRICHMENT ################")
print("############################################################")

"############### ADD NEW COLUMN ###############"

print("\nAmount has been added to the dataframe!")


df_cl['Amount'] = df_cl['UnitPrice'] * df_cl['Quantity']

df_cl = df_cl[[
                'InvoiceNo',
                'InvoiceDate',
                'StockCode',
                'Description',
                'Quantity',
                'UnitPrice',
                'Amount',
                'CustomerID',
                'Country']]

df_headers = df_cl.head()
print(df_headers)

print("\nYear,Month,Day, and Hour have been added to the dataframe!")

df_cl['InvoiceDate']=pd.to_datetime(df_cl['InvoiceDate'])

dayOfWeek={0:'Mon', 1:'Tue', 2:'Wed', 3:'Thur', 4:'Fri', 5:'Sat', 6:'Sun'}

df_cl['Month']  =pd.DatetimeIndex(df_cl['InvoiceDate']).month
df_cl['Year']   =pd.DatetimeIndex(df_cl['InvoiceDate']).year
df_cl['Day']    =pd.DatetimeIndex(df_cl['InvoiceDate']).dayofweek.map(dayOfWeek)
df_cl['Hour']   =pd.DatetimeIndex(df_cl['InvoiceDate']).hour


df_cl = df_cl[[
                'InvoiceNo',
                'InvoiceDate',
                'Year',
                'Month',
                'Day',
                'Hour',
                'StockCode',
                'Description',
                'Quantity',
                'UnitPrice',
                'Amount',
                'CustomerID',
                'Country']]

df_headers = df_cl.head()
print(df_headers)


print("\n############################################################")
print("################### STEP 3 - DATA ANALYSIS #################")
print("############################################################")

print("\n################ Trailing Twelve Month Chart for Service A ################")

Y_M = df_cl.groupby(['Month']).count().reset_index()

Y_Analysis = Y_M[['Month', 'InvoiceNo']]
Y_Analysis.columns = ['Month', 'Orders']

print(Y_Analysis)

plt.subplots(figsize=(13,7))
plt.bar(Y_Analysis.Month, Y_Analysis.Orders)
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.title('Service A Order Status (TTM)')
plt.show()

print("\n################ #Orders by Country ################")

C_M = df_cl.groupby(['Country']).count().reset_index()
C_AN = C_M[['Country','InvoiceNo']]

print("\nTop 10 Countries that orders were made the most:")
print(C_AN.nlargest(10, 'InvoiceNo').reset_index())


print("\n################ Who is the Key Revenue driver? ################")

KeyRev = df_cl.groupby(by=['Country'], as_index=False)['Amount'].sum()
NewKR = KeyRev.sort_values(by='Amount', ascending=False).head()

plt.subplots(figsize=(13,7))
plt.plot(NewKR.Country, NewKR.Amount)
plt.xlabel('Countries')
plt.ylabel('Amount (Dollar)')
plt.title('Sales amount for top Countries')
plt.show()

print("The Key Revenue driver is United Kingdom")

print("\n################ What's the most popular item in UK? ################")


new=df_cl[(df_cl["Country"]=="United Kingdom")]
new=new.groupby(["Country","Description"]).size()
maximum=new.sort_values(ascending=False)
print("The most popular item in the top sales country, UK:")
print("We should focus on these products in UK:")
print(maximum.head(5))
print()

print("In general, Service A doing great in European countries but we should extend our service to other Non-European countries.")

print("\n################ Who is the next After UK? ################")

afterUK = df_cl.groupby('Country')['InvoiceNo'].count().sort_values(ascending=False)
del afterUK['United Kingdom']
print(afterUK)


print("\n################ #Orders by specific Customers ################")

CU = df_cl.groupby(['CustomerID','Country']).count().reset_index()
CU_AN = CU[['CustomerID','Country','InvoiceNo']]

print("\nTop 10 Customers who ordered our products the most:")
print(CU_AN.nlargest(10, 'InvoiceNo').reset_index())


Cl_amt = df_cl.groupby(by=['CustomerID','Country'], as_index=False)['Amount'].sum()
VIP = Cl_amt.sort_values(by='Amount', ascending=False).head()
print(VIP)

print("It seems there are clients who order a lot of Service A products in Netherlands, UK. We should work with our Marketing and Sales teams to suggest more products to them")


print("\n################ #Orders by Different Days ################")

days = df_cl.groupby('InvoiceNo')['Day'].unique().value_counts().sort_index().plot(kind='bar',figsize=(12,6))

days.set_xlabel('Day')
days.set_ylabel('Orders')
days.set_title('Numer of orders for different Days')
plt.show()

print("The number of orders for Sunday is about a half of Monday's order. To improve our sales, we need to boost up the amount of orders for Sunday.")



print("\n################ #Orders throughout the Day(per Hour) ################")

hrs = df_cl.groupby('InvoiceNo')['Hour'].unique().value_counts().plot(kind='bar', figsize=(12,6))
print(hrs)

hrs.set_xlabel('Hour')
hrs.set_ylabel('Orders')
hrs.set_title('Numer of orders for different Hours')
plt.show()


print("According to the hourly breakdown of orders, customers are likely to order our services between 10AM and 3PM. If we foucs on this pattern, we will be able to attract more customers and it will bring more orders. ")