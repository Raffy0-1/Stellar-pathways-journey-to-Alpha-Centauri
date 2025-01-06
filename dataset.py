import random
import pandas as pd
from datetime import datetime, timedelta

# Define the areas
areas = ['Astraeon Basin', 'Helios Ridge', 'Elysium Crater']

# Function to simulate temperature
def simulate_temperature(time, area):
    """
    Simulates temperature variations over time for each area.
    The temperature will follow a diurnal cycle (higher in the day, lower at night).
    """
    base_temp = random.uniform(-10, 30)  # Random base temperature for the area
    time_of_day = time.hour + time.minute / 60  # Convert time to hours for simplicity

    # Temperature variation: Highest in the middle of the day, lowest at night
    daily_cycle = 10 * (1 - abs(12 - time_of_day) / 12)  # Simple model: 12pm highest temp

    # Adding the base temperature and daily cycle fluctuation
    return base_temp + daily_cycle

# Function to generate and save the dataset
def generate_and_save_data():
    # Starting time for the data collection (2025-01-01 00:00)
    time_start = datetime(2025, 1, 1, 0, 0)
    
    # Loop through each area to generate data
    for area in areas:
        area_data = []
        
        # Collect data for 24 hours, every 30 minutes (48 intervals)
        for i in range(48):  # 48 half-hour intervals in 24 hours
            time = time_start + timedelta(minutes=i * 30)
            
            # Simulate various attributes for each time interval
            temperature = simulate_temperature(time, area)
            oxygen = random.uniform(10, 30)
            soil_quality = random.uniform(0, 10)
            water_presence = random.uniform(0, 100)
            uv_radiation = random.uniform(0, 10)  # mW/cm²
            wind_speed = random.uniform(0, 10)  # m/s
            soil_nutrients = random.uniform(0, 10)  # Nutrient value
            pressure = random.uniform(0, 10)  # Atmospheric pressure in arbitrary units
            solar_radiation = random.uniform(0, 1500)  # W/m²
            gravity = random.uniform(0.5, 1.5)  # Gravitational force in g
            
            # Add the data for the current time interval (without time column)
            area_data.append({
                'Temperature': temperature,
                'Oxygen_Percentage': oxygen,
                'Soil_Quality': soil_quality,
                'Water_Presence': water_presence,
                'UV_Radiation': uv_radiation,
                'Wind_Speed': wind_speed,
                'Soil_Nutrients': soil_nutrients,
                'Pressure': pressure,
                'Solar_Radiation': solar_radiation,
                'Gravity': gravity
            })
        
        # Convert the area data into a DataFrame and save it to CSV (without Time column)
        df = pd.DataFrame(area_data)
        df.to_csv(f'{area}_data.csv', index=False)
        print(f"Data for {area} saved to CSV.")

# Run the program to generate and save the dataset
if __name__ == "__main__":
    generate_and_save_data()
