# Lekcja 11 - Zadanie 9
# Uruchom: python zadanie_09.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

age_sum = 0.0
age_count = 0
for numer, chunk in enumerate(pd.read_csv(URL, chunksize=100), start=1):
    print(f"Batch {numer}: {len(chunk)} wierszy, średni wiek: {chunk['Age'].mean():.2f}")
    age_sum += chunk["Age"].sum()
    age_count += chunk["Age"].count()
print(f"Globalna średnia wieku: {age_sum / age_count:.2f}")
