import requests
from datetime import datetime
import pandas as pd
import os

lat = 10.75
lon = 106.6667
APIkey = '7a11d0dc5b39eccc81c453338085c028'  # Replace with your actual OpenWeatherMap API key

# Define start and end dates (as Unix timestamps)
# Adjusting date range to the last 5 years, as an example
start_date = datetime(2018, 1, 1).timestamp()
end_date = datetime(2024, 5, 31).timestamp()

# Construct the API URL with parameters
apiKey = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={int(start_date)}&end={int(end_date)}&appid={APIkey}'

# Make the API request
response = requests.get(apiKey)

# Check if the request was successful
if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

data = response.json()

# Prepare to store monthly averages
monthly_averages = {
    'Month': [],
    'AQI': [],
    'co': [],
    'no': [],
    'no2': [],
    'o3': [],
    'so2': [],
    'pm2_5': [],
    'pm10': [],
    'nh3': []
}

monthly_data = {}

# Aggregate data into monthly averages
for entry in data['list']:
    dt = datetime.utcfromtimestamp(entry['dt'])
    month_key = dt.strftime('%Y-%m')

    if month_key not in monthly_data:
        monthly_data[month_key] = {component: [] for component in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']}
        monthly_data[month_key]['AQI'] = []
    
    for component in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
        monthly_data[month_key][component].append(entry['components'][component])
    monthly_data[month_key]['AQI'].append(entry['main']['aqi'])

# Calculate monthly averages
for month in monthly_data:
    monthly_averages['Month'].append(month)
    for component in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
        monthly_averages[component].append(sum(monthly_data[month][component]) / len(monthly_data[month][component]))
    monthly_averages['AQI'].append(sum(monthly_data[month]['AQI']) / len(monthly_data[month]['AQI']))

# Create DataFrame from monthly averages
df = pd.DataFrame(monthly_averages)

# Export data to Excel
excel_file = 'hcm_air_pollution_data_monthly.xlsx'
# Delete the file if it exists
if os.path.exists(excel_file):
    os.remove(excel_file)
    print(f"Old {excel_file} deleted.")
    
df.to_excel(excel_file, index=False)

print(f"Data has been exported to {excel_file}")
