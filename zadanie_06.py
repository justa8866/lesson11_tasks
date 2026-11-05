# Lekcja 11 - Zadanie 6
# Uruchom: python zadanie_06.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
srednia = df["Age"].mean()
print(f"Średnia przed uzupełnieniem: {srednia:.2f}")
print("Braki przed:", df["Age"].isna().sum())
df["Age"] = df["Age"].fillna(srednia)
print("Braki po:", df["Age"].isna().sum())
print("Czy wszystkie wartości Age są obecne?", df["Age"].notna().all())
