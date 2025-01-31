# Import libraries 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import csv
import os
# Input parameters
# Input = Amino acid sequence, window size
user_input = input("Type your amino acid sequence: ") 
window = input("window size: ") # which window size are considereds  and why only those? 
window = int(window) 
# If the user mistakenly typed any lower characters during inputting sequence, converts them into upper characters
user_input = user_input.upper() 
length = len(user_input)
# Does sequence matching and allots a particular hydropathy score for every amino acid in the inputted sequence by using values stored in the score dictionary.
array = []
scores = {'G':0.00,'C':1.15,'I':0.97,'L':0.87,'F':0.85,'V':0.83,'W':0.67,'Y':0.60,'M':0.54,'A':0.33,'P':0.32,'H':0.25,'T':0.21,'S':0.05,'R':-0.01,'Q':-0.05,'N':-0.07,'D':-0.22,'E':-0.24,'K':-0.40}
#amino_acid = {'Gly': 'G', 'Cys': 'C', 'Ile': 'I', 'Leu': 'L', 'Phe': 'F','Val': 'V', 'Trp': 'W','Tyr': 'Y', 'Met': 'M', 'Ala': 'A', 'Pro': 'P', 'His': 'H', 'Thr': 'T', 'Ser': 'S', 'Arg': 'R', 'Gln': 'Q', 'Asn': 'N', 'Asp': 'D', 'Glu': 'E', 'Lys': 'K'}
# the loop appends the input sequences and allot the scores based on the amino acid sequence
# x is an variable
with open("3GBN_3.csv", "w", newline='') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=['Aminoacid','Hydrophobicityscore'], delimiter = ',')
	writer.writeheader()
	for x in user_input:
			array.append(scores[x])
			writer.writerow({'Aminoacid': x, 'Hydrophobicityscore': scores[x]})
	#print(scores[x]) # check the scores alloted to the amino acid sequence
print("CSV file stored in:", os.getcwd())
# Plot the graph
yaxis=[] 
# count return the number of times an object appears in a list 
# sum = returns a number, the sum of all items in an iterable.
count = 0
sum = 0
for x in array:
	sum = x+sum 
	count=count+1
	# % modulus divides left hand operand by right hand operand and returns remainder
	if count%window==0:
		yaxis.append(sum/window)
		sum=0 
print ("Length of amino acid sequence: %d" %(length)) 
print ("Window Size: %d" %(window))
y_axis= np.array(yaxis) # y_axis is converted to numpy array to represent in either in form of vectors, matrices and tensors
#print(y_axis.shape)
#print(y_axis.ndim)
length = length - length%window 
#print(length)
t = np.arange(0, length, window)
#print(t)
x_axis=np.array(t)#.reshape(1,-1)
#print(x_axis.shape)
#print(x_axis.ndim)
#print(x_axis)
print ("Number of points plotted: %d" %(len(x_axis))) 


fig, ax = plt.subplots() # create multiple layout of the subplots
ax.plot(x_axis, y_axis)
		#print(ax.plot)
ax.set(xlabel='Amino acid sequence position', ylabel='Hydrophobicity score', title=''' PDB_ID- 3GBN Bandyopadhyay-Mehler Hydropathy plot ''')
ax.grid() # configure the grid lines
image_format = 'svg'
image_name = 'myimage.svg'
fig.savefig(image_name, format=image_format, dpi=1200) 
plt.show()




