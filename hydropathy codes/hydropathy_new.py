# Import libraries 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import csv

# Input parameters
# Input = Amino acid sequences, window size
num_sequences = int(input("Enter the number of sequences you want to analyze: "))
sequences = []

for i in range(num_sequences):
    user_input = input(f"Type your amino acid sequence {i + 1}: ") 
    user_input = user_input.upper()  # Convert to uppercase
    sequences.append(user_input)

window = int(input("Enter the window size: "))

# Hydropathy scores dictionary
scores = {'G':0.00,'C':1.15,'I':0.97,'L':0.87,'F':0.85,'V':0.83,'W':0.67,'Y':0.60,'M':0.54,'A':0.33,'P':0.32,'H':0.25,'T':0.21,'S':0.05,'R':-0.01,'Q':-0.05,'N':-0.07,'D':-0.22,'E':-0.24,'K':-0.40}

# Process each sequence
for idx, user_input in enumerate(sequences):
    print(f"Processing sequence {idx + 1}...")  # Confirm processing of each sequence
    length = len(user_input)
    array = []

    # Write scores to a CSV file
    csv_filename = f"results_sequence_{idx + 1}.csv"
    with open(csv_filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Aminoacid', 'Hydrophobicityscore'], delimiter=',')
        writer.writeheader()
        for x in user_input:
            array.append(scores[x])
            writer.writerow({'Aminoacid': x, 'Hydrophobicityscore': scores[x]})

    # Calculate hydropathy scores using a sliding window
    yaxis = []
    count = 0
    sum = 0
    for x in array:
        sum += x
        count += 1
        if count % window == 0:
            yaxis.append(sum / window)
            sum = 0

    # Prepare X and Y axes
    y_axis = np.array(yaxis)
    length_adjusted = length - (length % window)
    t = np.arange(0, length_adjusted, window)
    x_axis = np.array(t)

    # Plot the graph
    print(f"Sequence {idx + 1}: Length = {length}, Window size = {window}, Points plotted = {len(x_axis)}")
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis)
    ax.set(xlabel='Amino acid sequence position', ylabel='Hydrophobicity score',
           title=f'Sequence {idx + 1} Hydropathy Plot')
    ax.grid()

    # Save the plot to a file
    image_name = f"hydropathy_sequence_{idx + 1}.svg"
    fig.savefig(image_name, format='svg', dpi=1200)

    # Display and close the plot
    plt.draw()
    plt.pause(3)  # Adjust pause duration as needed
    plt.close(fig)  # Ensure this figure is closed

print("All sequences processed successfully!")
