# import modules
import pandas as pd
import numpy as np
from datetime import date
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# read the store and training data from the csv
df = pd.read_csv("train.csv", low_memory=False)
store = pd.read_csv("store.csv", low_memory=False)

# Merge training data and store data based on 'Store' column
# Store the merged data in a variable called 'data'
data = df.merge(store, on = ['Store'], how='inner')

# Print distinct # of stores
# Print distinct # of Dates
# Print the average daily sales of all Stores combined
print('Distinct number of Stores:', len(data['Store'].unique()))
print('Distinct number of Dates:', len(data['Date'].unique()))
print('Average daily sales of all Stores:', round(data['Sales'].mean(), 2))

# Print the amount of sales on each Day labeled 1 through 7
print(data['DayOfWeek'].value_counts())

# Adjust Date column values to a more usable format
data['Date'] = pd.to_datetime(data['Date'])

# Creating seperate columns for Year, Month, Quarter, Week and Day from Data column values
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Quarter'] = data['Date'].dt.quarter
data['Week'] = data['Date'].dt.isocalendar().week
data['Day'] = data['Date'].dt.day

# Print newly addedd columns. Addition shows the year, month, quarter, week, day and season of each record.
# print(data.iloc[:,-6:])

data['CompetitionDistance'] = data['CompetitionDistance'].fillna(0, inplace = True)

data.set_index('Store')

print(data.head())

# data.loc(data['Season'] == 'Summer', 'Sales').sum()

# Show histogram
#plt.hist(data['Sales'])
#plt.title('Histogram of Store Sales')
#plt.ylabel('bins')
#plt.xlabel('frequency')
#plt.show()

#data.hist(figsize = (20,15))
#plt.show()

