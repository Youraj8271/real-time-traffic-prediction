import pandas as pd
import random
from datetime import datetime, timedelta

# Parameters
locations = ['Patna Junction', 'Bailey Road', 'Kankarbagh', 'Gandhi Maidan', 'Boring Road']
weather_options = ['Clear', 'Rain', 'Fog']
road_types = ['Highway', 'City', 'Bridge']

# Generate fake data
data = []
start_time = datetime(2025, 7, 1, 6, 0)  # Start from 6 AM
for i in range(300):
    timestamp = start_time + timedelta(minutes=15 * i)
    location = random.choice(locations)
    vehicle_count = random.randint(20, 200)
    avg_speed = round(random.uniform(10, 50), 2)
    weather = random.choice(weather_options)
    road_type = random.choice(road_types)
    data.append([timestamp, location, vehicle_count, avg_speed, weather, road_type])

# Create DataFrame
df = pd.DataFrame(data, columns=['timestamp', 'location', 'vehicle_count', 'avg_speed', 'weather', 'road_type'])

# Save to CSV
df.to_csv('data/traffic_data.csv', index=False)
print("✅ Dataset generated successfully!")
