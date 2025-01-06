import pandas as pd
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from datetime import datetime, timedelta

# Load datasets
def load_data():
    farming_data = pd.read_csv("Farming_Rover_Area_data.csv")
    recycling_data = pd.read_csv("Recycling_Rover_Area_data.csv")
    return farming_data, recycling_data

# Preprocess farming data
def preprocess_farming_data(farming_data):
    label_encoders = {}
    for col in ['Crop_Type', 'Soil_Condition', 'Weather_Condition']:
        le = LabelEncoder()
        farming_data[col] = le.fit_transform(farming_data[col])
        label_encoders[col] = le

    # Drop the 'Time' column as it is not numerical
    farming_data = farming_data.drop(columns=['Time'])
    return farming_data, label_encoders

# Preprocess recycling data
def preprocess_recycling_data(recycling_data):
    # Drop the 'Time' column as it is not numerical
    recycling_data = recycling_data.drop(columns=['Time'])
    return recycling_data

# Train a model for farming rover
def train_farming_model(farming_data):
    X = farming_data.drop(columns=["Crop_Health"])
    y = farming_data["Crop_Health"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Train a model for recycling rover
def train_recycling_model(recycling_data):
    X = recycling_data.drop(columns=["Waste_Reduction"])
    y = recycling_data["Waste_Reduction"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Generate random conditions for farming and recycling rovers
def generate_random_conditions():
    farming_conditions = {
        "Temperature": random.uniform(15, 35),
        "Precipitation": random.uniform(0, 100),
        "Sunlight": random.uniform(3, 12),
        "Soil_Quality": random.uniform(3, 10),
        "Crop_Type": random.randint(0, 4),  # Encoded values (e.g., Wheat=0, Rice=1, etc.)
        "Soil_Condition": random.randint(0, 4),
        "Weather_Condition": random.randint(0, 4)
    }
    recycling_conditions = {
        "Water_Quality": random.uniform(30, 100),
        "Nutrient_Levels": random.uniform(0, 100),
        "Oxygen_Content": random.uniform(20, 100),
        "Water_Level": random.uniform(0, 100)
    }
    return farming_conditions, recycling_conditions

# Make predictions
def make_predictions(farming_model, recycling_model, farming_conditions, recycling_conditions):
    farming_input = pd.DataFrame([farming_conditions])
    recycling_input = pd.DataFrame([recycling_conditions])

    farming_output = farming_model.predict(farming_input)[0]
    recycling_output = recycling_model.predict(recycling_input)[0]

    return farming_output, recycling_output

# Main program
def main():
    # Load data
    farming_data, recycling_data = load_data()

    # Preprocess data
    farming_data, label_encoders = preprocess_farming_data(farming_data)
    recycling_data = preprocess_recycling_data(recycling_data)

    # Train models
    farming_model = train_farming_model(farming_data)
    recycling_model = train_recycling_model(recycling_data)

    # Generate random conditions
    farming_conditions, recycling_conditions = generate_random_conditions()

    # Make predictions
    farming_output, recycling_output = make_predictions(farming_model, recycling_model, farming_conditions, recycling_conditions)

    # Decode the categorical labels for display
    crop_types = label_encoders["Crop_Type"].inverse_transform([farming_conditions["Crop_Type"]])[0]
    soil_conditions = label_encoders["Soil_Condition"].inverse_transform([farming_conditions["Soil_Condition"]])[0]
    weather_conditions = label_encoders["Weather_Condition"].inverse_transform([farming_conditions["Weather_Condition"]])[0]

    # Display outputs
    print("\n=== Farming Rover Output ===")
    print(f"Conditions: Temperature={farming_conditions['Temperature']:.2f}°C, "
          f"Precipitation={farming_conditions['Precipitation']:.2f}mm, "
          f"Sunlight={farming_conditions['Sunlight']:.2f}hrs, "
          f"Soil_Quality={farming_conditions['Soil_Quality']:.2f}, "
          f"Crop_Type={crop_types}, "
          f"Soil_Condition={soil_conditions}, "
          f"Weather_Condition={weather_conditions}")
    print(f"Predicted Crop Health: {farming_output:.2f}")

    print("\n=== Recycling Rover Output ===")
    print(f"Conditions: Water_Quality={recycling_conditions['Water_Quality']:.2f}%, "
          f"Nutrient_Levels={recycling_conditions['Nutrient_Levels']:.2f}%, "
          f"Oxygen_Content={recycling_conditions['Oxygen_Content']:.2f}%, "
          f"Water_Level={recycling_conditions['Water_Level']:.2f}%")
    print(f"Predicted Waste Reduction Efficiency: {recycling_output:.2f}")

# Run the main program
if __name__ == "__main__":
    main()
