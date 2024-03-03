import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind


# Initialize lists to store values from the 'Time' column
values = []
values2 = []

# Initialize lists to store values
resultLatest = []
resultLegacy = []

def parse():
    for i in range(1, 33):
        filename = f"experiment/win32/2024-02-27-00-04-07/chrome/react-latest/{i}.csv"
    
        # Open the CSV file
        with open(filename, newline='') as csvfile:
            # Create a CSV reader object
            csvreader = csv.DictReader(csvfile)
            
            # Iterate over each row in the CSV file
            for row in csvreader:
                # Each row is a dictionary where keys are column names
                values.append(int(row['PACKAGE_ENERGY (J)']))
                values2.append(int(row['Time']))

            # Find the maximum and minimum values from the list
            valueDifference = max(values) - min(values)
            valueDifference2 = max(values2) - min(values2)

            #resultLatest.append(valueDifference * pow(valueDifference2, 10))
            resultLatest.append(valueDifference)
            #print(valueDifference)
            values.clear()
            values2.clear()

    print("===================")

    for i in range(33, 65):
        filename = f"experiment/win32/2024-02-27-00-04-07/chrome/react-legacy/{i}.csv"

        # Open the CSV file
        with open(filename, newline='') as csvfile:
            # Create a CSV reader object
            csvreader = csv.DictReader(csvfile)
            
            # Iterate over each row in the CSV file
            for row in csvreader:
                # Each row is a dictionary where keys are column names
                values.append(int(row['PACKAGE_ENERGY (J)']))
                values2.append(int(row['Time']))

            # Find the maximum and minimum values from the list
            valueDifference = max(values) - min(values)
            valueDifference2 = max(values2) - min(values2)

            resultLegacy.append(valueDifference * pow(valueDifference2, 10))
            #print(valueDifference)
            values.clear()
            values2.clear()
    
    return resultLatest, resultLegacy


def graph(resultsLatest, resultsLegacy):
    # Create a list of data for both cases
    data = [resultsLatest, resultsLegacy]

    # Create the box plot
    box = plt.boxplot(data, patch_artist=True, medianprops=dict(color="black"))

    # Manually set box colors
    box_colors = ['#218c74', '#33d9b2']
    for patch, color in zip(box['boxes'], box_colors):
        patch.set_facecolor(color)

    # Add labels and title
    plt.xticks([1, 2], ['react-latest', 'react-legacy'])
    plt.ylabel('EDP')
    plt.title('Energy Delay Product (EDP), w=10')

    # Show the plot
    plt.grid(False)
    plt.show()

def reject_outliers(data, m = 9.):
    data = np.array(data)  # Convert list to NumPy array
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d / mdev if mdev else np.zeros(len(d))
    return data[s < m].tolist()  # Convert back to list before returning

"""
def p_value(distribution1, distribution2):
    # Perform a t-test
    t_statistic, p_value = ttest_ind(distribution1, distribution2)

    print("t-statistic:", t_statistic)
    print("p-value:", p_value)
    print("len(dist1): ", len(distribution1))
    print("len(dist2): ", len(distribution2))

    """

def main():
    data1, data2 = parse()
   
    data1 = reject_outliers(data1)
    data2 = reject_outliers(data2)
    graph(data1, data2)

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
