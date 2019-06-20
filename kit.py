import pandas as pd
from matplotlib import pyplot as plt

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

#This is the number of solar flares detected in the csv file
n = 0
#Sentinalls
flareStarted = False
flareEnded = True

for i in range(1, count_row):
    #if (data.A_AVG[i] > t1 and flareStarted == False):
    if(df.A_AVG[i] - df.A_AVG[i-1] >= t1 and flareStarted == False):
        n += 1
        print("Solar Flare #" + str(n))
        print("Start time: " + str(df.time_tag[i]))
        flareStarted = True
        flareEnded = False

    #if(data.A_AVG[i] < t1 and flareEnded == False):
    if(df.A_AVG[i] - df.A_AVG[i-1] < -t1 and flareEnded == False):
        print("End time:   " + str(df.time_tag[i]))
        print("=====")
        flareEnded = True
        flareStarted = False

print("Finished Analyzing Data")
if (n == 0):
    print("There were no detectable solar flares in this data set")

plt.plot(df.A_AVG)
plt.show()
