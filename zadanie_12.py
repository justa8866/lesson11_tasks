# Lekcja 11 - Zadanie 12
# Uruchom: python zadanie_12.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
przed = df.memory_usage(deep=True).sum()
opt = df.copy()
for kol in ["Pclass", "Survived", "SibSp", "Parch"]:
    opt[kol] = opt[kol].astype("int8")
for kol in ["Sex", "Embarked"]:
    opt[kol] = opt[kol].astype("category")
po = opt.memory_usage(deep=True).sum()
print(f"Pamięć przed: {przed} B ({przed / 1024:.2f} KB)")
print(f"Pamięć po: {po} B ({po / 1024:.2f} KB)")
print(f"Redukcja: {(1 - po / przed) * 100:.2f}%")
