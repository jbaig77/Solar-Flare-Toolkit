import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#these two functions find the max peak and time of a solar flare
def findmaxtime (df, starting, ending):
    n = len(data)
    maxval = df.A_AVG[starting]
    maxindex = starting
    for i in range(starting,ending):
        if (df.A_AVG[i] > maxval):
            maxval = df.A_AVG[i]
            maxindex = i
    return df.time_tag[maxindex]

def findmaxPeak (df, starting, ending, list):
    n = len(data)
    maxval = df.A_AVG[starting]
    maxindex = starting
    for i in range(starting,ending):
        if (df.A_AVG[i] > maxval):
            maxval = df.A_AVG[i]
            maxindex = i
    list.append(df.A_AVG[maxindex])
    return df.A_AVG[maxindex]


#Asking user for input
interval = input("Please enter how many points you would like to skip. The number you enter must be greater than zero and an integer: ")
k1 = int(interval)
t = input("Please enter the threshold for positive detection: ")
t1 = float(t)

#Formalst csv to only have the data and nothing else.
with open('flare.csv') as f:
    for i, line in enumerate(f):
        if line.startswith('data:'):
            break
d = pd.read_csv('flare.csv', skiprows=i+1)
d.to_csv('out.csv', index=False)


data = pd.read_csv('out.csv')
#Replaces all values of -99999 with 0
data['A_AVG'].replace([-99999], [0], inplace=True)
data['B_AVG'].replace([-99999], [0], inplace=True)

#Compressess data by reading every 'k'th row
data2 = data[data.index % k1 == 0]
data2.to_csv('workingData.csv', index=False)

df = pd.read_csv('workingData.csv')

#This finds out how many rows are in the csv file, not including the header row.
count_row = df.shape[0] 

#Opening a text file to save output to
f = open('flareoutput.txt','w')

f.write("Chosen Interval: " + str(k1) + '\n')
f.write("Chosen threshold for detection: " + str(t1) + '\n')
f.write("===========")


#This is the number of solar flares detected in the csv file
n = 0
#Sentinalls
flareStarted = False
flareEnded = True


#list that contains all the peak flares
peakFlares = []

for i in range(1, count_row):
    #if (data.A_AVG[i] > t1 and flareStarted == False):
    if(df.A_AVG[i] - df.A_AVG[i-1] >= t1 and flareStarted == False):
        n += 1
        print("Solar Flare #" + str(n))
        print("Start time: " + str(df.time_tag[i]))

        f.write("\nSolar Flare #" + str(n) + "\nStart time: " + str(df.time_tag[i]))

        flareStartPH = i #Index of a flare when it starts

        flareStarted = True
        flareEnded = False

    #if(data.A_AVG[i] < t1 and flareEnded == False):
    if(df.A_AVG[i] - df.A_AVG[i-1] < -t1 and flareEnded == False):
        print("End time:   " + str(df.time_tag[i]))

        f.write("\nEnd time:   " + str(df.time_tag[i]) + '\n')

        flareEndPH = i #Index of a flare when it ends

        print("The max peak index is at: ")
        print(findmaxtime(df,flareStartPH,flareEndPH))

        f.write("The max peak index is at: \n" + findmaxtime(df,flareStartPH,flareEndPH) + '\n')

        print("The value at this time is: ")
        print(findmaxPeak(df,flareStartPH,flareEndPH, peakFlares))

        f.write("The value at this time is: \n" + str(findmaxPeak(df,flareStartPH,flareEndPH, peakFlares)) + '\n')

        print("=====")

        #print(df.iloc[flareStartPH:flareEndPH, df.A_AVG].max())

        flareEnded = True
        flareStarted = False

print("Finished Analyzing Data")
if (n == 0):
    print("There were no detectable solar flares in this data set")

f.close()

#Create a new csv with only the datapoints that are solar flares
dff = pd.DataFrame(peakFlares,columns =['FlarePeaks'])
dff['LogValue'] = np.log10(dff['FlarePeaks'])
dff.to_csv('sfDataPoints.csv', index=False)

