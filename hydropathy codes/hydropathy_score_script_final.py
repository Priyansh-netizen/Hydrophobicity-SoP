# Import libraries 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import csv
import os

# Input parameters
# Input = Amino acid sequence
user_input = input("Type your amino acid sequence: ") 
user_input = user_input.upper()  # Convert input sequence to uppercase
length = len(user_input)

# Hydrophobicity scores
data_folder = "3GBN_4_hydropathy_scores"
os.makedirs(data_folder, exist_ok=True)  # Create directory if not exists

# Dictionary of hydropathy scores
scores = {'G': 0.00, 'C': 1.15, 'I': 0.97, 'L': 0.87, 'F': 0.85, 'V': 0.83, 'W': 0.67, 'Y': 0.60, 'M': 0.54, 
          'A': 0.33, 'P': 0.32, 'H': 0.25, 'T': 0.21, 'S': 0.05, 'R': -0.01, 'Q': -0.05, 'N': -0.07, 
          'D': -0.22, 'E': -0.24, 'K': -0.40}

# Check for invalid characters
if any(x not in scores for x in user_input):
    raise ValueError("Invalid amino acid sequence!")

for window in range(3, 14):  # Loop through window sizes 3 to 13
    array = []
    # Generate hydrophobicity scores
    for x in user_input:
        array.append(scores[x])

    # Prepare CSV file for the current window size
    file_name = os.path.join(data_folder, f"3GBN_4_win_{window}.csv")
    with open(file_name, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Aminoacid', 'Hydrophobicityscore'], delimiter=',')
        writer.writeheader()
        for x, score in zip(user_input, array):
            writer.writerow({'Aminoacid': x, 'Hydrophobicityscore': score})

    # Calculate hydropathy scores for the window
    yaxis = []
    count = 0
    sum = 0
    for x in array:
        sum = x + sum
        count += 1
        if count % window == 0:
            yaxis.append(sum / window)
            sum = 0

    # Adjust length for plotting
    trimmed_length = length - length % window
    t = np.arange(0, trimmed_length, window)
    x_axis = np.array(t)
    y_axis = np.array(yaxis)

    # Plot the graph for the current window
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis)
    ax.set(xlabel='Amino acid sequence position', ylabel='Hydrophobicity score',
           title=f'''PDB_ID- 3GBN_4 Bandyopadhyay-Mehler Hydropathy plot (Window Size: {window})''')
    ax.grid()

    # Save the plot
    image_name = os.path.join(data_folder, f"3GBN_4_win_{window}.svg")
    fig.savefig(image_name, format='svg', dpi=1200)
    plt.close(fig)  # Close the figure to avoid memory overload

print(f"Hydropathy scores and plots saved in folder: {data_folder}")
