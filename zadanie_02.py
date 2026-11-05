# Lekcja 11 - Zadanie 2
# Uruchom: python zadanie_02.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
print("Informacje:")
df.info()
print("\nStatystyki:\n", df.describe())
print(f"\nŚredni wiek: {df['Age'].mean():.2f} lat")
