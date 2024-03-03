import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def extract_energy(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        energy_values = [float(row['PACKAGE_ENERGY (J)']) for row in reader]
    return energy_values[-1] - energy_values[0]

def get_creation_time(file_path):
    return os.path.getctime(file_path)

def plot_energy_over_time(folder_paths):
    plt.figure(figsize=(10, 6))

    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']  # Define colors for folders
    names = ['react-legacy', 'react-latest', 'dummy']
    for i, folder_path in enumerate(folder_paths):
        folder_data = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                file_path = os.path.join(folder_path, file_name)
                creation_time = get_creation_time(file_path)
                total_energy = extract_energy(file_path)
                folder_data.append((creation_time, total_energy))

        folder_data.sort(key=lambda x: x[0])
        creation_times, total_energies = zip(*folder_data)
        plt.scatter(creation_times, total_energies, color=colors[i], label=names[i])

        # Fit a trendline
        x = np.array(creation_times)
        y = np.array(total_energies)
        slope, intercept, _, _, _ = stats.linregress(x, y)
        plt.plot(x, slope*x + intercept, color=colors[i])

    plt.xlabel('Creation Time')
    plt.ylabel('Total Energy (J)')
    plt.title('Total Energy over Creation Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    folder_paths = ["experiment/win32/2024-02-27-00-04-07/firefox/react-legacy", "experiment/win32/2024-02-27-00-04-07/firefox/react-latest"]  # Update with your folder paths
    plot_energy_over_time(folder_paths)
