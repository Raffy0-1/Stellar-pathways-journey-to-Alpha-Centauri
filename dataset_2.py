import random
import pandas as pd
from datetime import datetime, timedelta

# Define possible parameters for both rovers
crops = ['Wheat', 'Rice', 'Corn', 'Soybean', 'Potato']
soil_conditions = ['Sandy', 'Clay', 'Loamy', 'Peaty', 'Saline']
weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Stormy', 'Windy']

# Function to simulate farming data
def simulate_farming_data(time, area):
    base_temp = random.uniform(15, 35)  # Temperature range (°C)
    precipitation = random.uniform(0, 100)  # Precipitation (mm)
    sunlight = random.uniform(3, 12)  # Sunlight hours
    soil_quality = random.uniform(3, 10)  # Soil quality index (1-10 scale)
    crop_type = random.choice(crops)
    soil_condition = random.choice(soil_conditions)
    weather_condition = random.choice(weather_conditions)
    
    # Simulate crop health based on weather and soil conditions
    crop_health = 100 - abs(soil_quality - random.uniform(3, 10)) * 5 - abs(base_temp - 25) * 2 + random.uniform(0, 20)
    
    return {
        'Time': time,
        'Temperature': base_temp,
        'Precipitation': precipitation,
        'Sunlight': sunlight,
        'Soil_Quality': soil_quality,
        'Crop_Type': crop_type,
        'Soil_Condition': soil_condition,
        'Weather_Condition': weather_condition,
        'Crop_Health': crop_health
    }

# Function to simulate recycling data
def simulate_recycling_data(time):
    water_quality = random.uniform(30, 100)  # Water quality (percentage)
    nutrient_levels = random.uniform(0, 100)  # Nutrient levels in water
    oxygen_content = random.uniform(20, 100)  # Oxygen content (percentage)
    water_level = random.uniform(0, 100)  # Water level (percentage)
    waste_reduction = random.uniform(0, 100)  # Waste reduction (percentage)
    
    return {
        'Time': time,
        'Water_Quality': water_quality,
        'Nutrient_Levels': nutrient_levels,
        'Oxygen_Content': oxygen_content,
        'Water_Level': water_level,
        'Waste_Reduction': waste_reduction
    }

# Function to generate and save both rovers' data
def generate_and_save_data():
    # Define the areas and starting time
    areas = ['Farming_Rover_Area', 'Recycling_Rover_Area']
    time_start = datetime(2025, 1, 1, 0, 0)
    
    # Collect data for both rovers
    for area in areas:
        area_data = []
        
        # Loop through 365 days, collecting data every 6 hours (4 intervals per day)
        for i in range(365 * 4):  # 365 days * 4 intervals per day
            time = time_start + timedelta(hours=i * 6)
            
            if area == 'Farming_Rover_Area':
                # Generate farming-related data
                data_point = simulate_farming_data(time, area)
            elif area == 'Recycling_Rover_Area':
                # Generate recycling-related data
                data_point = simulate_recycling_data(time)
            
            # Add the data point for the current time interval
            area_data.append(data_point)
        
        # Convert the data into a DataFrame and save it to CSV
        df = pd.DataFrame(area_data)
        df.to_csv(f'{area}_data.csv', index=False)
        print(f"Data for {area} saved to CSV.")

# Run the program to generate and save both rovers' datasets
if __name__ == "__main__":
    generate_and_save_data()
