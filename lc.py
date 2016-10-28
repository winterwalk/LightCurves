'''
This is the newest version of lc.py.

'''

import matplotlib.pyplot as plt
import numpy as np
from math import floor
from scipy.optimize import curve_fit

datafile = open ('kepler.dat')
kdata = datafile.readlines()
datafile.close()

timeList = []
fluxList = []

# Populates lists with file data:

for line in kdata:
    ph = line.split()
    timeList.append(float(ph[0]))
    fluxList.append(float(ph[1]))
print("len(timeList) = ", len(timeList))

# Gaussian function definition:

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

# Notable constants, arrays declared here:
P = 1.76358757 #OrbitalPeriod
FirstTimeValue = timeList[0]
FirstCentroid = 0.42
NumberOfPeriods = int(np.ceil(((timeList[-1])-(timeList[0]))/ P))
timeArray = np.array(timeList)
timeArray = timeArray - timeArray[0]
print(timeArray[0])
fluxArray = np.array(fluxList)
for i in range(0, NumberOfPeriods):
    found = np.where((timeArray > i * P) & (timeArray < (i + 1) * P))
    croppedTimeArray = timeArray[found]
    croppedFluxArray = fluxArray[found]
    p0 = [-5, (FirstCentroid + (i * P)), 0.3]
    plt.plot(croppedTimeArray, croppedFluxArray, 'o')
    plt.show()
    popt, pcov = curve_fit (gauss, croppedTimeArray, croppedFluxArray, p0)
    print("fit = ", popt)
    print("guess = ", p0)
    plt.plot(croppedTimeArray, gauss(croppedTimeArray, *popt))
    plt.show()
