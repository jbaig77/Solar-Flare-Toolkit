import datetime
import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt

df0 = pd.read_csv('workingData.csv')

xray = df0['A_AVG']

xray_fft = sp.fftpack.fft(xray)
xray_psd = np.abs(xray_fft) ** 2

fftfreq = sp.fftpack.fftfreq(len(xray_psd), 1. / 8928)

i = fftfreq > 0

plt.plot(fftfreq)
plt.show()