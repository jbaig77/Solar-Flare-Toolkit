import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('workingData.csv')
df['A_AVG'].plot()
plt.show()