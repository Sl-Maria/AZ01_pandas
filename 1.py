import pandas as pd
import numpy as np

df = pd.read_csv('FOOD-DATA-GROUP1.csv')

df.drop('Unnamed: 0.1', axis=1, inplace=True)
df.drop('Unnamed: 0', axis=1, inplace=True)
print(df.head())

print(df.info())
print(df.describe())