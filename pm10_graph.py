import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_excel('hanoi_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'pm10'])
df2 = pd.read_excel('hcm_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'pm10'])
df3 = pd.read_excel('vn_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'pm10'])

# Convert the 'Month' and 'co' columns of the DataFrames to lists
months1 = df1['Month'].tolist()
co_values1 = df1['pm10'].tolist()
months2 = df2['Month'].tolist()
co_values2 = df2['pm10'].tolist()
months3 = df3['Month'].tolist()
co_values3 = df3['pm10'].tolist()

# Plotting the data from the first file
plt.plot(months1, co_values1, label='Hanoi', color='blue')

plt.plot(months2, co_values2, label='HCM', color='red')

plt.plot(months3, co_values3, label='AVG', color='green')

# Naming the x axis
plt.xlabel('Month')
# Naming the y axis
plt.ylabel('pm10')

# Giving a title to the graph
plt.title('pm10 Comparison inside VN')

# Adding a legend to distinguish between the two lines
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Function to show the plot
plt.show()
