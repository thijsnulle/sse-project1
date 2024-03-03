import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
from dataclasses import dataclass
from scipy.stats import shapiro, ttest_ind
import numpy as np

energy_types = ['dram_energy', 'package_energy', 'pp0_energy', 'pp1_energy', 'power']

@dataclass
class DataPoint:
    dram_energy: float
    package_energy: float
    pp0_energy: float
    pp1_energy: float
    power: float

def get_data_points():
    folders = [ 
        os.path.join('data', x)
        for x in os.listdir('data')
        if os.path.isdir('data/' + x)
    ]

    data = dict()
    for folder in folders:
        data[folder] = []
        csv_files = [ x for x in os.listdir(folder) if x.endswith('.csv') ][2:]

        for csv_file in csv_files:
            data_points = []

            with open(os.path.join(folder, csv_file), 'r') as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    data_points.append(DataPoint(
                        dram_energy=float(row[18]),
                        package_energy=float(row[19]),
                        pp0_energy=float(row[20]),
                        pp1_energy=float(row[21]),
                        power=0
                    ))

            total_dram = data_points[-1].dram_energy - data_points[0].dram_energy
            total_package = data_points[-1].package_energy - data_points[0].package_energy
            total_pp0 = data_points[-1].pp0_energy - data_points[0].pp0_energy
            total_pp1 = data_points[-1].pp1_energy - data_points[0].pp1_energy
            power = total_package / (len(data_points) * 0.2)

            data[folder].append(DataPoint(
                dram_energy=total_dram,
                package_energy=total_package,
                pp0_energy=total_pp0,
                pp1_energy=total_pp1,
                power=power
            ))

    return data

def print_plots(data):
    # Create subplots for each energy type
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)

    # Extract energy types
    energy_types = ['dram_energy', 'package_energy', 'pp0_energy', 'power']

    for i, ax_row in enumerate(axes):
        for j, ax in enumerate(ax_row):
            # Extract data for the current energy type
            energy_type = energy_types[i * 2 + j]
            energy_data = {folder: [getattr(dp, energy_type) for dp in data_points] for folder, data_points in data.items()}
            
            # Create violin plot
            sns.violinplot(data=list(energy_data.values()), ax=ax)
            ax.set_title(energy_type)

            xtick_labels = [folder.split('/')[-1] for folder in data.keys()]
            ax.set_xticklabels(xtick_labels, rotation=45, ha='right')

            if (i == 1) and (j == 1):
                ax.set_ylabel('Power (W)')
            else:
                ax.set_ylabel('Energy (J)')

    plt.tight_layout()
    plt.savefig('energy_violin_plots.png')

    plt.show()

def shapiro_test(data):
    for folder, data_points in data.items():
        print(folder)
        for energy_type in energy_types:
            energy_data = [getattr(dp, energy_type) for dp in data_points]

            print(energy_type, 'p =', shapiro(energy_data).pvalue)
        print()

def t_test(data):
    d1 = data['data/react-legacy']
    d2 = data['data/react-latest']

    for energy_type in energy_types:
        energy_data1 = [getattr(dp, energy_type) for dp in d1]
        energy_data2 = [getattr(dp, energy_type) for dp in d2]

        t_stat, p_value = ttest_ind(energy_data1, energy_data2, equal_var=False, alternative='two-sided')

        print(energy_type, 't =', t_stat)
        print(energy_type, 'p =', p_value)
        print()

def mean_percent_diff(data):
    d2 = data['data/react-legacy']
    d1 = data['data/react-latest']

    for energy_type in energy_types:
        energy_data1 = [getattr(dp, energy_type) for dp in d1]
        energy_data2 = [getattr(dp, energy_type) for dp in d2]

        mean1 = np.mean(energy_data1)
        mean2 = np.mean(energy_data2)

        print(energy_type, 'mean1 =', mean1)
        print(energy_type, 'mean2 =', mean2)
        print(energy_type, 'mean percent diff =', (mean1 - mean2) / mean1 * 100)

    print()

def cohen_d(data):
    d1 = data['data/react-legacy']
    d2 = data['data/react-latest']

    for energy_type in energy_types:
        energy_data1 = [getattr(dp, energy_type) for dp in d1]
        energy_data2 = [getattr(dp, energy_type) for dp in d2]

        s1 = np.std(energy_data1)
        s2 = np.std(energy_data2)

        n1 = len(energy_data1)
        n2 = len(energy_data2)

        s = np.sqrt(((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2))

        d = (np.mean(energy_data1) - np.mean(energy_data2)) / s

        print(energy_type, 'd =', d)
    print()

def filter_data_points(data):
    for folder, data_points in data.items():
        std = {energy_type: np.std([getattr(dp, energy_type) for dp in data_points]) for energy_type in energy_types}
        mean = {energy_type: np.mean([getattr(dp, energy_type) for dp in data_points]) for energy_type in energy_types}

        # filter the data points where the (mean - value) > 3 * std
        for energy_type in energy_types:
            data_points = [dp for dp in data_points if abs(getattr(dp, energy_type) - mean[energy_type]) < 3 * std[energy_type]]

        data[folder] = data_points

    return data

if __name__ == '__main__':
    data = get_data_points()
    data = filter_data_points(data)

    shapiro_test(data)
    t_test(data)
    cohen_d(data)
    mean_percent_diff(data)
    print_plots(data)
