import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('workingData.csv')

#plt.plot(data.A_AVG)
#plt.show()

window = 10
#m represents how many solar flares were recorded
n = 0
flareStarted = False
flareEnded = False
for i in range (0,44640):
#for i, row in data.iterrows():
    #This is a weird way of interating through the column, my indexing solutions are iffy and bad practice. This should be fixed later.
    #i += 1
    #if(i != 44640): #this is a temporary fix, this is the last line of the csv file to prevent an out of bounds error.

    #if (data.A_AVG[i] > 1e-7 and flareStarted == False):    
    if(data.A_AVG[i] - data.A_AVG[i-1] >= 1e-7 and flareStarted == False):
        n += 1
        print("Solar Flare #" + str(n))
        print("Start time: " + str(data.time_tag[i]))
        flareStarted = True
        flareEnded = False

    #if(data.A_AVG[i] < 1e-7 and flareEnded == False):
    if(data.A_AVG[i] - data.A_AVG[i-1] < -1e-7 and flareEnded == False):
        print("End at time " + str(data.time_tag[i]))
        print("=====")
        flareEnded = True
        flareStarted = False

    #else:
        #print("Finished Analyzing Data")

print("Finished Analyzing Data")
if (n == 0):
    print("There were no detectable solar flares in this data set")
