import matplotlib

import matplotlib.pyplot as plt 
import numpy as np
user_input = input("Type your amino acid sequence: ") 
window = input("window size: ")
print('''Enter for abraham for black..28 for eisen''')
menu = input("menu: ") 
menu = int(menu) 
window = int(window)
user_input = user_input.upper() 
length = len(user_input) 
array1 = []
array2=[]
bandomehler = {'G':0.00,'C':1.15,'I':0.97,'L':0.87,'F':0.85,'V':0.83,'W':0.67,'Y':0.60,'M':0.54,'A':0.33,'P':0.32,'H':0.25,'T':0.21,'S':0.05,'R':-0.01,'Q':- 0.05,'N':-0.07,'D':-0.22,'E':-0.24,'K':-0.40}
abraham={'A':0.440,'R':-2.420,'N':-1.320,'D':-0.310,'C':0.580,'Q':-0.710,'E':-0.340,'G':0.000,'H':-0.010,'I':2.460,'L':2.460,'K':- 2.450,'M':1.100,'F':2.540,'P':1.290,'S':-0.840,'T':-0.410,'W':2.560,'Y':1.630,'V':1.730}
black={'A':0.616,'R':0.000,'N':0.2360,'D':0.0280,'C':0.680,'Q':0.251,'E':0.043,'G':0.501,'H':0.165,'I':1.800,'L':0.943,'K':0.283,'M':0.738,'F':1.000,'P':0.711,'S':0.359,'T':0.450,'W':0.878,'Y':0.880,'V':0.825}
eisenberg={'A':0.620,'R':-2.530,'N':-0.780,'D':-0.900,'C':0.290,'Q':- 0.850,'E':-0.740,'G':0.480,'H':-0.400,'I':1.380,'L':1.060,'K':- 1.500,'M':0.640,'F':1.190,'P':0.120,'S':-0.180,'T':- 0.050,'W':0.810,'Y':0.260,'V':1.080}
cowmanph75={'A':0.350,'R':-1.500,'N':-0.990,'D':-2.150,'C':0.760,'Q':- 0.930,'E':-1.950,'G':0.00,'H':-0.650,'I':1.830,'L':1.800,'K':- 1.540,'M':1.100,'F':1.690,'P':0.840,'S':-0.630,'T':-0.270,'W':1.350,'Y':0.390,'V':1.320}
cowmanph34= {'A':0.420,'R':-1.560,'N':-1.030,'D':-0.510,'C':0.840,'Q':- 0.960,'E':-0.370,'G':0.000,'H':-2.280,'I':1.810,'L':1.800,'K':- 2.030,'M':1.180,'F':1.740,'P':0.860,'S':-0.640,'T':- 0.260,'W':1.460,'Y':0.510,'V':1.340}
bull= {'A':0.610,'R':0.690,'N':0.890,'D':0.610,'C':0.360,'Q':0.970,'E': 0.510,'G':0.810,'H':0.690,'I':-1.450,'L':-1.650,'K':0.460,'M':- 0.660,'F':-1.520,'P':- 0.170,'S':0.420,'T':0.290,'W':-1.200,'Y':- 1.430,'V':-0.750}
hopp= {'A':-0.500,'R':3.000,'N':0.200,'D':3.000,'C':- 1.000,'Q':0.200,'E':3.000,'G':0.000,'H':-0.500,'I':-1.800,'L':-1.800,'K':3.000,'M':-1.300,'F':- 2.500,'P':0.000,'S':0.300,'T':- 0.400,'W':-3.400,'Y':-2.300,'V':-1.500}
manavalan={'A':12.970,'R':11.720,'N':11.420,'D':10.850,'C':14.630,'Q':11.760,'E':11.890,'G':12.430,'H':12.610,'I':15.670,'L':14.900,'K':11.360,'M':14.390,'F':14.000,'P':11.370,'S':11.230,'T':11.690,' W':13.930,'Y':13.420,'V':15.710}
guy= {'A':0.100,'R':1.910,'N':0.480,'D':0.780,'C':- 1.420,'Q':0.950,'E':0.830,'G':0.330,'H':-0.500,'I':-1.130,'L':- 1.180,'K':1.400,'M':-1.590,'F':- 2.120,'P':0.730,'S':0.520,'T':0.070,'W':-0.510,'Y':-0.210,'V':- 1.270}
kyte= {'A':1.800,'R':-4.500,'N':-3.500,'D':-3.500,'C':2.500,'Q':- 3.500,'E':-3.500,'G':-0.400,'H':-3.200,'I':4.500,'L':3.800,'K':-3.900,'M':1.900,'F':2.800,'P':-1.600,'S':-0.800,'T':-0.700,'W':- 0.900,'Y':-1.300,'V':4.200}
miyazava= {'A':5.330,'R':4.180,'N':3.710,'D':3.590,'C':7.930,'Q':3.870,'E': 3.650,'G':4.480,'H':5.100,'I':8.830,'L':8.470,'K':2.950,'M':8.950,'F':9.030,'P':3.870,'S':4.090,'T':4.490,'W':7.660,'Y':5.890,'V' :7.630}
mobility ={'A':5.100,'R':2.000,'N':0.600,'D':0.700,'C':0.000,'Q':1.400,'E': 1.800,'G':4.100,'H':1.600,'I':9.300,'L':10.000,'K':1.300,'M':8.700,'F':9.600,'P':4.900,'S':3.100,'T':3.500,'W':9.200,'Y':8.000,' V':8.500}
roseman ={'A':0.390,'R':-3.950,'N':-1.910,'D':-3.810,'C':0.250,'Q':- 1.300,'E':-2.910,'G':0.000,'H':-0.640,'I':1.820,'L':1.820,'K':- 2.770,'M':0.960,'F':2.270,'P':0.990,'S':-1.240,'T':- 1.000,'W':2.130,'Y':1.470,'V':1.300}
wilson ={'A':-0.300,'R':-1.100,'N':-0.200,'D':-1.400,'C':6.300,'Q':- 0.200,'E':0.000,'G':1.200,'H':-1.300,'I':4.300,'L':6.600,'K':- 3.600,'M':2.500,'F':7.500,'P':2.200,'S':-0.600,'T':- 2.200,'W':7.900,'Y':7.100,'V':5.900}
wolfenden= {'A':1.940,'R':-19.920,'N':-9.680,'D':-10.950,'C':-1.240,'Q':-9.380,'E':-10.200,'G':2.390,'H':-10.270,'I':2.150,'L':2.280,'K':- 9.520,'M':- 1.480,'F':-0.760,'P':0.000,'S':-5.060,'T':-4.880,'W':-5.880,'Y':-6.110,'V':1.990}
fauchere ={'A':0.310,'R':-1.010,'N':-0.600,'D':-0.770,'C':1.540,'Q':- 0.220,'E':-0.640,'G':0.000,'H':0.130,'I':1.800,'L':1.700,'K':- 0.990,'M':1.230,'F':1.790,'P':0.720,'S':- 0.040,'T':0.260,'W':2.250,'Y':0.960,'V':1.220}
janin={'A':0.300,'R':-1.400,'N':-0.500,'D':-0.600,'C':0.900,'Q':- 0.700,'E':-0.700,'G':0.300,'H':-0.100,'I':0.700,'L':0.500,'K':- 1.800,'M':0.400,'F':0.500,'P':-0.300,'S':-0.100,'T':-0.200,'W':0.300,'Y':-0.400,'V':0.600}
rao={'A':1.360,'R':0.150,'N':0.330,'D':0.110,'C':1.270,'Q':0.330,'E':0.250,'G':1.090,'H':0.680,'I':1.440,'L':1.470,'K':0.090,'M':1.420,'F': 1.570,'P':0.540,'S':0.970,'T':1.080,'W':1.000,'Y':0.830,'V':1.370}
tanford= {'A':0.620,'R':-2.530,'N':-0.780,'D':-0.090,'C':0.290,'Q':- 0.850,'E':-0.740,'G':0.480,'H':-0.400,'I':1.380,'L':1.530,'K':- 1.500,'M':0.640,'F':1.190,'P':0.120,'S':-0.180,'T':- 0.050,'W':0.810,'Y':0.260,'V':1.800}
parker={'A':2.100,'R':4.200,'N':7.000,'D':10.00,'C':1.400,'Q':6.00,'E':7.800,'G':5.700,'H':2.100,'I':-8.000,'L':9.200,'K':5.700,'M':- 4.200,'F':- 9.200,'P':2.100,'S':6.500,'T':5.200,'W':-10.00,'Y':- 1.900,'V':-3.700}
welling={'A':1.150,'R':0.580,'N':-0.770,'D':0.650,'C':-1.200,'Q':- 0.110,'E':-0.710,'G':-1.840,'H':3.120,'I':- 2.920,'L':0.750,'K':2.060,'M':-3.850,'F':- 1.410,'P':-0.530,'S':- 0.260,'T':-0.450,'W':-1.140,'Y':0.130,'V':-0.130}
faulp = {'G':-0.40,'C':1.54,'I':1.8,'L':1.7,'F':1.79,'V':1.22,'W':2.25,'Y':0.96,'M':1.23,'A':0.31,'P':0.72,'H':0.13,'T':0.26,'S':-0.04,'R':-1.01,'Q':-0.22,'N':- 0.6,'D':-0.77,'E':-0.64,'K':-0.99}
abodr = {'G':- 0.40,'C':0.00,'I':9.3,'L':10.0,'F':9.6,'V':8.5,'W':9.2,'Y':8.0,'M':8.7,'A':5.1,'P':4.9,'H':1.6,'T':3.5,'S':3.1,'R':2.0,'Q':1.4,'N':0.6,'D':0.7,'E':1.8,'K':1.3}
rose = {'G':- 0.40,'C':0.91,'I':0.88,'L':0.85,'F':0.88,'V':0.86,'W':0.85,'Y':0.76,'M':0.85,'A':0.74,'P':0.64,'H':0.78,'T':0.70,'S':0.66,'R':0.64,'Q':0.62,'N':0.63,'D':0.62,'E':0.62,'K':0.52}
ponnu = {'G':- 0.40,'C':14.93,'I':14.77,'L':14.10,'F':13.43,'V':15.07,'W':12.95,'Y':13.29,'M':14.33,'A':12.28,'P':11.19,'H':12.84,'T':11.65,'S':11.26,'R':11.49,'Q':11.28,'N'
:11.00,'D':10.97,'E':11.19,'K':10.80}
mijer = {'G':- 0.40,'C':7.93,'I':8.83,'L':8.47,'F':9.03,'V':7.73,'W':7.66,'Y':5.89,'M':8.95,'A':5.33,'P':3.87,'H':5.1,'T':4.49,'S':4.09,'R':4.18,'Q':3.87,'N':3.71,'D':3.59,'E':3.65,'K':2.95}
white = {'G':-0.40,'C':-0.02,'I':-1.12,'L':-1.25,'F':-1.71,'V':-0.46,'W':-2.09,'Y':-0.71,'M':-
0.67,'A':0.50,'P':0.14,'H':2.33,'T':0.25,'S':0.46,'R':1.81,'Q':0.77,'N':0.85,'D':3.64,'E':3.63,'K':2.8}
eisen= {'G':-0.40,'C':0.38,'I':1.90,'L':1.90,'F':2.30,'V':1.50,'W':2.60,'Y':1.60,'M':2.40,'A':0.67,'P':1.20,'H':0.64,'T':0.52,'S':0.01,'R':-2.10,'Q':-0.22,'N':-0.6,'D':-1.2,'E':-0.76,'K':-0.57}

scores={0:bandomehler,1:abraham,2:black,3:eisenberg,4:cowmanph75,5:cowmanph34,6:bull,7:hopp,8:manavalan,9:guy,10:kyte,11:miyazava,12:mobility,13:roseman,14:wilson,15:wolfenden,16:fauchere,17:janin,18:rao,19:tanford,20:parker,21:welling,22:faulp,23:abodr,24:rose,25:ponnu,26:mijer,27:white,28:eisen}

for x in user_input: 
	array1.append(scores[0][x])
for x in user_input: 
	array2.append(scores[menu][x])
yaxis1=[] 
yaxis2=[] 
count = 0
sum1=0 
sum2=0
for x in array1:
	sum1 = x+sum1 
	count=count+1
	if count%window==0: 
		yaxis1.append(sum1/window) 
		sum1=0
count = 0
for x in array2:
	sum2 = x+sum2 
	count=count+1
	if count%window==0:
		yaxis2.append(sum2/window) 
		sum2=0
one = np.array(yaxis1) 
two = np.array(yaxis2)
coeff=np.corrcoef(one,two) 
print(coeff[1][0]) 
matplotlib.style.use('ggplot') 
fig, ax = plt.subplots()
ax.set(xlabel='Bandyopadhyay-Mehler ', ylabel='Selected', title=''' Correlation coefficient ''')
ax.grid() 
plt.scatter(one,two) 
plt.show()




