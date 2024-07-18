import pandas as pd

df = pd.read_csv('dz.csv')
print(df)

# df.dropna(inplace=True)   # не влияет на результат группировки и вычисление mean
# print(df.head(12))

group = df.groupby('City')['Salary'].mean()
print(group)