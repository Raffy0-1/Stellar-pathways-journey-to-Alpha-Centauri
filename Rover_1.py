import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time

# Load the datasets for the three areas
def load_data():
    areas = ['Astraeon Basin', 'Helios Ridge', 'Elysium Crater']
    data = {}
    
    for area in areas:
        try:
            df = pd.read_csv(f'{area}_data.csv')  # Load the CSV file for each area
            print(f"Loaded {area} data with columns: {df.columns}")
            data[area] = df
        except Exception as e:
            print(f"Error loading data for {area}: {e}")
        
    return data

# Preprocess the data (normalize, handle missing values, etc.)
def preprocess_data(df):
    df.fillna(df.mean(), inplace=True)
    features = ['Temperature', 'Oxygen_Percentage', 'Soil_Quality', 'Water_Presence', 
                'UV_Radiation', 'Wind_Speed', 'Soil_Nutrients', 'Pressure', 
                'Solar_Radiation', 'Gravity']
    missing_cols = [col for col in features if col not in df.columns]
    if missing_cols:
        print(f"Missing columns: {missing_cols}")
        return None, None
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])
    return scaled_data, df

def define_labels(data):
    scores = {area: data[area]['Oxygen_Percentage'].mean() + data[area]['Soil_Quality'].mean() for area in data}
    best_area = max(scores, key=scores.get)
    return best_area

def train_model(data):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    X = []
    y = []
    for area, df in data.items():
        X_area, _ = preprocess_data(df)
        if X_area is None:
            continue
        best_area = define_labels(data)
        y_area = [1 if area == best_area else 0] * len(df)
        X.extend(X_area)
        y.extend(y_area)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    return model

def visualize_feature_importance(model):
    feature_importances = model.feature_importances_
    features = ['Temperature', 'Oxygen_Percentage', 'Soil_Quality', 'Water_Presence', 
                'UV_Radiation', 'Wind_Speed', 'Soil_Nutrients', 'Pressure', 
                'Solar_Radiation', 'Gravity']
    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importances, y=features)
    plt.title('Feature Importance for Area Sustainability Prediction')
    plt.xlabel('Importance')
    plt.ylabel('Features')
    plt.show()

# Add spice with randomized rover messages and actions
def show_rover_message(stage):
    messages = {
        "start": ["Rover initializing...", "Beginning search for sustainable areas...", "Scanning planet surface..."],
        "processing": ["Analyzing data streams...", "Compiling oxygen and soil quality metrics...", "Evaluating life sustainability scores..."],
        "found": [f"Area found! Deploying farming rover (Rover 2)...", f"Optimal area detected! Activating recycling unit (Rover 3)..."],
        "end": [f"Mission success! Area marked for colonization.", f"Operation complete! Suitable zone secured."]
    }
    print(random.choice(messages[stage]))
    time.sleep(2)

# Run the rover analysis with dynamic messages
def rover_analysis():
    show_rover_message("start")
    data = load_data()
    model = train_model(data)
    visualize_feature_importance(model)
    area_predictions = {area: model.predict(preprocess_data(df)[0]) for area, df in data.items()}
    predicted_best_area = max(area_predictions, key=lambda area: area_predictions[area].sum())
    show_rover_message("found")
    print(f"The most sustainable area for life is: {predicted_best_area}")
    show_rover_message("end")

if __name__ == "__main__":
    rover_analysis()
