# Lekcja 11 - Zadanie 10
# Uruchom: python zadanie_10.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
print("Przed:", df.shape)
print("Age przed:\n", df["Age"].describe())
clean = df.copy()
clean = clean.loc[:, clean.isna().mean() <= 0.60].copy()
clean["Age"] = clean["Age"].fillna(clean["Age"].median())
clean["Embarked"] = clean["Embarked"].fillna(clean["Embarked"].mode().iloc[0])
clean = clean.dropna()
print("\nPo:", clean.shape)
print("Liczba pozostałych NaN:", clean.isna().sum().sum())
print("Age po:\n", clean["Age"].describe())
