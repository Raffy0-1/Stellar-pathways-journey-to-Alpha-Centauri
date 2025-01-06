import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


LIGHT_SPEED = 299792458  # Speed light in m/s.
GRAVITATIONAL_CONSTANT = 6.67430e-11
DISTANCE_ALPHA_CENTAURI = 4.367 * 9.46e15

def calculate_travel_time(warp_factor): # Calculate  traveling time.
    if warp_factor < 1:
        raise ValueError("Warp factor must be >= 1")
    time_in_seconds = DISTANCE_ALPHA_CENTAURI / (warp_factor * LIGHT_SPEED)
    time_in_years = time_in_seconds / (60 * 60 * 24 * 365)
    return time_in_years


def calculate_energy_requirement(warp_factor):
    volume_bubble = 1e12  # Volume warp bubble  and Negative energy density.
    energy_density = -1e-9
    energy = volume_bubble * energy_density * (warp_factor**3)
    return energy


def simulate_obstacles(travel_time_years): # obstacle in our journey.
    obstacles = ["Meteor Shower", "Gravitational Anomaly", "Cosmic Radiation"]
    encountered_obstacle = np.random.choice(obstacles)
    obstacle_energy_multiplier = {
        "Meteor Shower": 1.1,
        "Gravitational Anomaly": 1.2,
        "Cosmic Radiation": 1.15,
    }
    return encountered_obstacle, obstacle_energy_multiplier[encountered_obstacle]

def simulate_journey(warp_factor):
    travel_time = calculate_travel_time(warp_factor)
    energy_required = calculate_energy_requirement(warp_factor)

    obstacle, multiplier = simulate_obstacles(travel_time)
    energy_required *= multiplier
    return travel_time, energy_required, obstacle


def visualize_warp_bubble(): # warp bubble in space fabric.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='purple', alpha=0.7)
    ax.set_title("Warp Bubble Visualization")
    plt.show()


def animate_journey(warp_factor):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

                  # Initial positions on shuttle in bubble.
    x = [0]
    y = [0]
    z = [0]

    def update(num):
        x.append(num * warp_factor * 1e12)
        y.append(np.sin(num * 0.1) * 1e11)
        z.append(np.cos(num * 0.1) * 1e11)
        ax.clear()
        ax.scatter(x, y, z, color="purple", label="Rocket Position")
        ax.set_title("Journey to Alpha Centauri")
        ax.legend()

    ani = FuncAnimation(fig, update, frames=100, repeat=False)
    plt.show()

             #  -----------------plots--------------------#
                      #1
def plot_energy_vs_warp():
    warp_factors = np.linspace(1, 10, 100)
    energies = [calculate_energy_requirement(wf) for wf in warp_factors]
    plt.plot(warp_factors, energies, color='green')
    plt.title("Energy Requirement vs Warp Factor")
    plt.xlabel("Warp Factor")
    plt.ylabel("Energy (Joules)")
    plt.show()

                      #2
def plot_travel_time_vs_warp():
    warp_factors = np.linspace(4, 10, 100)
    times = [calculate_travel_time(wf) for wf in warp_factors]
    plt.plot(warp_factors, times, color='blue')
    plt.title("Travel Time vs Warp Factor")
    plt.xlabel("Warp Factor")
    plt.ylabel("Travel Time (Years)")
    plt.show()

                      #3
def plot_resource_depletion(initial_population, resources):
    growth_rate = 1
    years = 2
    population = initial_population
    resource_levels = []
    for year in range(1, years + 1):
        population *= growth_rate
        resources -= population * 100
        resource_levels.append(resources if resources > 0 else 0)
    plt.plot(range(1, years + 1), resource_levels, color='green')
    plt.title("Colony Resource Depletion")
    plt.xlabel("Years")
    plt.ylabel("Remaining Resources")
    plt.show()

                      #4
def plot_trajectory_2d(warp_factor):
    t = np.linspace(0, 10, 100)
    x = warp_factor * t * 1e12
    y = np.sin(t) * 1e11
    plt.plot(x, y, color='purple')
    plt.title("Top-down View of Spacecraft Trajectory")
    plt.xlabel("X Position (meters)")
    plt.ylabel("Y Position (meters)")
    plt.show()

                       #5
def plot_obstacle_frequency(simulations=10):
    obstacles = ["Meteor Shower", "Gravitational Anomaly", "Cosmic Radiation"]
    counts = {obstacle: 0 for obstacle in obstacles}
    for _ in range(simulations):
        obstacle, _ = simulate_obstacles(1)
        counts[obstacle] += 1
    plt.bar(counts.keys(), counts.values(), color='lightblue')
    plt.title("Obstacle Frequency in Simulations")
    plt.ylabel("Frequency")
    plt.show()

# colony for rovers limit alarm.
def colony_setup(initial_population, resources):
    growth_rate = 1.0
    years = 2
    population = initial_population
    for year in range(1, years + 1):
        population *= growth_rate
        resources -= population * 100
        if resources <= 0:
            return f"Colony failed due to resource depletion in year {year}."
    return f"Colony established with population {int(population)} and resources {resources} remaining."

# Main function
def main():
    print("Welcome to the Alpha Centauri way to  New Life.✨️!")
    rocket_name = input("Enter the rocket name: ")
    warp_factor = float(input("Enter warp factor (1-10): "))
    initial_population = int(input("Enter the number of rovers those left spacecraft deck for research: "))
    resources = float(input("Enter total resources (10000/rover min): "))

    try:

        travel_time, energy_required, obstacle = simulate_journey(warp_factor)
        print(f"\nJourney Details:")
        print(f"Warp Factor: {warp_factor}")
        print(f"Travel Time: {travel_time:.2f} years")
        print(f"Energy Required: {energy_required:.2e} joules")
        print(f"Obstacle Encountered: {obstacle}")
        visualize_warp_bubble()
        animate_journey(warp_factor)
        plot_energy_vs_warp()
        plot_travel_time_vs_warp()
        plot_resource_depletion(initial_population, resources)
        plot_trajectory_2d(warp_factor)
        plot_obstacle_frequency()


        colony_result = colony_setup(initial_population, resources)
        print(f"\nColony Setup Results: {colony_result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
   main()