# Lekcja 11 - Zadanie 3
# Uruchom: python zadanie_03.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
subset = df[["Name", "Age", "Sex", "Survived"]].copy()
print(subset.head(10).to_string(index=False))
subset.to_csv("titanic_subset.csv", index=False, encoding="utf-8-sig")
print("\nZapisano titanic_subset.csv")
