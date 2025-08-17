# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 23:39:08 2025

@author: sergi
"""

import pandas as pd

# Cargamos los datos de sales_data dentro de un datafram
sales_data = pd.read_excel('sales_data.xlsx')


# =============================================================================
# Exploring the data
# =============================================================================

 #Get a summary of sales data
 
sales_data.info()
sales_data.describe()

# Looking at the columns
print(sales_data.columns)

#Looking first rows
print(sales_data.head())

#Check datatype of each column
print(sales_data.dtypes)



# =============================================================================
# Cleaning Data
# =============================================================================

#Check missing Values
print(sales_data.isnull().sum())

#Vemos que account y currency tiene 7795 missing values
#deleterows that has any missing values
sales_data_clean = sales_data.dropna(subset = ['Amount'])

#Checkeamos si hay valoras faltantes en nuevstros data limpios
print(sales_data_clean.isnull().sum())



# =============================================================================
# Slicing and filtering Data
# =============================================================================


#Select a subset of our data based on the Category Column
category_data = sales_data[sales_data['Category'] == 'Top']
print(category_data)

#Select a subset of our data where the Amount > 1000
high_amount_data = sales_data[sales_data['Amount'] > 1000]
print(high_amount_data)

#Select a subset of data based on multiple conditions
filtered_data = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] == 3)]
    

# =============================================================================
# Aggregating Data
# =============================================================================

#total sales by category
category_totals = sales_data.groupby('Category')['Amount'].sum()
category_totals = sales_data.groupby('Category', as_index=False)['Amount'].sum()
category_totals = category_totals.sort_values('Amount', ascending=False)

#calculate the average Amount by Category and Fulfilment
fulfilment_averages = sales_data.groupby(['Category', 'Fulfilment'], as_index=False)['Amount'].mean()
fulfilment_averages = fulfilment_averages.sort_values('Amount', ascending=False)

#calculate the average Amount by Category and Status
status_averages = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean()
status_averages = status_averages.sort_values('Amount', ascending=False)

#calculate total sales by shipment and fulfilment
total_sales_shipandfulfil = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_shipandfulfil = total_sales_shipandfulfil.sort_values('Amount', ascending=False)
total_sales_shipandfulfil.rename(columns={'Courier Status': 'Shipment'}, inplace=True)



# =============================================================================
# Exporting the Data
# =============================================================================
status_averages.to_excel('average_sales_by_category_and_status.xlsx', index=False)
total_sales_shipandfulfil.to_excel('total_sales_by_ship_and_fulfil.xlsx', index=False)



















