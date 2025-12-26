import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")
# Output: Temperature in Paris: 20.0°C

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
india_temp = get_weather(28.61, 77.20)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
print(f"India: {india_temp}°C")

import requests
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

import pandas as pd

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

import matplotlib.pyplot as plt

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

import os

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")

# Complete Code


import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# 1. Get weather data
today = datetime.now()
week_ago = today - timedelta(days=7)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

# 2. Process with pandas
df = pd.DataFrame({
    'date': pd.to_datetime(data['daily']['time']),
    'max_temp': data['daily']['temperature_2m_max'],
    'min_temp': data['daily']['temperature_2m_min']
})

# 3. Calculate average
df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2

# 4. Create visualization
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], 'r-o', label='Max')
plt.plot(df['date'], df['min_temp'], 'b-o', label='Min')
plt.plot(df['date'], df['avg_temp'], 'g--', label='Average')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past Week')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# 5. Save everything
if not os.path.exists('data'):
    os.makedirs('data')

plt.savefig('data/weather_chart.png')
df.to_csv('data/paris_weather.csv', index=False)

print(f"Average temperature: {df['avg_temp'].mean():.1f}°C")
print("Files saved in 'data' folder")



class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client

# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")

class APIClient:
    version = "1.0"              # Same for all clients
    max_retries = 3              # Same for all clients
    
    def __init__(self, api_key):
        self.api_key = api_key   # Unique to each client