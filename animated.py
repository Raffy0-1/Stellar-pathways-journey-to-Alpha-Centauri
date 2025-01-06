import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import random

# Import your existing functions from the main script
from rover_2_3 import (
    load_data,
    preprocess_farming_data,
    preprocess_recycling_data,
    train_farming_model,
    train_recycling_model,
    generate_random_conditions,
    make_predictions
)

# Initialize data
farming_data, recycling_data = load_data()
farming_data, label_encoders = preprocess_farming_data(farming_data)
recycling_data = preprocess_recycling_data(recycling_data)

farming_model = train_farming_model(farming_data)
recycling_model = train_recycling_model(recycling_data)

# Initialize Matplotlib figure and axes
fig, ax = plt.subplots()
x_data, y_data_farming, y_data_recycling = [], [], []

# Farming and recycling lines
line_farming, = ax.plot([], [], label="Farming Rover (Crop Health)", color="green")
line_recycling, = ax.plot([], [], label="Recycling Rover (Waste Reduction)", color="blue")

# Set plot limits and labels
ax.set_xlim(0, 50)  # Number of frames
ax.set_ylim(0, 100)  # Prediction range
ax.set_xlabel("Time (frames)")
ax.set_ylabel("Prediction Values")
ax.legend()

# Update function for animation
def update(frame):
    global x_data, y_data_farming, y_data_recycling

    # Generate random conditions
    farming_conditions, recycling_conditions = generate_random_conditions()
    
    # Make predictions
    farming_output, recycling_output = make_predictions(farming_model, recycling_model, farming_conditions, recycling_conditions)

    # Append new data
    x_data.append(frame)
    y_data_farming.append(farming_output)
    y_data_recycling.append(recycling_output)

    # Update the lines
    line_farming.set_data(x_data, y_data_farming)
    line_recycling.set_data(x_data, y_data_recycling)

    return line_farming, line_recycling

# Create animation
ani = FuncAnimation(fig, update, frames=range(50), blit=True, repeat=False)

# Display the animation
plt.show()
