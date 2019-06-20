import pandas as pd

with open('flare.csv') as f:
    for i, line in enumerate(f):
        if line.startswith('data:'):
            break
df = pd.read_csv('flare.csv', skiprows=i+1)
print(df.head())
df.to_csv('out.csv', index=False)
