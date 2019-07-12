import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import subplot

#Function the plots the bar graph
def plot_bar():
    subplot(1,2,2)
    index = np.arange(len(classes))
    plt.bar(index, flareid)
    plt.xlabel('Flare Class')
    plt.ylabel('No. of Solar Flares')
    plt.xticks(index, classes, rotation = 30)
    plt.title('Solar Flare Classification')

def plot_xray():
    subplot(1,2,1)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Xray Value (W/m^2)')
    plt.title('A_AVG graphed with time')
    df['A_AVG'].plot()


#Creating lists to classify solar flares
names = ['A Class', 'B Class', 'C Class', 'M Class', 'X Class']
numFlares = []

df = pd.read_csv('workingData.csv')
dff = pd.read_csv('sfDataPoints.csv')

#Creating new columns without pandas complaining about the colum/index size
la, lb, lc, ld = len(dff.FlarePeaks), len(names), len(dff.LogValue), len(numFlares)
max_len = max(la, lb, lc, ld)
if not max_len == la:
    dff.FlarePeaks.extend(['']*(max_len-la))
if not max_len == lb:
    names.extend(['']*(max_len-lb))
if not max_len == lc:
    dff.logvalue.extend(['']*(max_len-lc))
if not max_len == ld:
    numFlares.extend(['']*(max_len-ld))
dff = pd.DataFrame({'FlarePeaks':dff.FlarePeaks, 'LogValue':dff.LogValue, 'Classes':names, 'FlareIdentity':numFlares})


#Classifying the solar flares based on their class
it = len(dff.FlarePeaks)
a = 0
b= 0
c = 0
m = 0
x = 0
for i in range(0,it):
    if(dff.LogValue[i] > -8 and dff.LogValue[i] <= -7):
        #A Class
        a = a+1
    if(dff.LogValue[i] > -7 and dff.LogValue[i] <= -6):
        #B Class
        b = b+1
    if(dff.LogValue[i] > -6 and dff.LogValue[i] <= -5):
        #C Class
        c = c+1
    if(dff.LogValue[i] > -5 and dff.LogValue[i] <= -4):
        #M Class
        m = m+1
    if(dff.LogValue[i] > -4 and dff.LogValue[i] <= -3):
        #X Class
        x = x+1
dff.FlareIdentity[0] = a
dff.FlareIdentity[1] = b
dff.FlareIdentity[2] = c
dff.FlareIdentity[3] = m
dff.FlareIdentity[4] = x

#Saves to csv
dff.to_csv('sfDataPoints.csv', index=False)

#Converts dataframe colums back into a list for plotting
classes = list(dff.Classes)
flareid = list(dff.FlareIdentity)

while("" in classes):
    classes.remove("")
while("" in flareid):
    flareid.remove("")

#Plot the bargraph showing the solar flare classifications
plt.figure(1)
plot_bar()
plot_xray()

plt.show()