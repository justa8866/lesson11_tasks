# Lekcja 11 - Zadanie 7
# Uruchom: python zadanie_07.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
posortowane = df.sort_values("Age", ascending=True, na_position="last")
print("10 najmłodszych:\n", posortowane[["Name", "Age"]].head(10).to_string(index=False))
print("\n10 najstarszych:\n", posortowane.dropna(subset=["Age"])[["Name", "Age"]].tail(10).sort_values("Age", ascending=False).to_string(index=False))
