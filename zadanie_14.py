# Lekcja 11 - Zadanie 14
# Uruchom: python zadanie_14.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
mask = df.isnull()
print("Mapa braków: X=NaN, .=wartość")
print("Kolumny:", " | ".join(df.columns))
for idx, row in mask.head(30).iterrows():
    print(f"{idx:3d}: " + "  ".join("X" if x else "." for x in row))
for kol in ["Cabin", "Embarked"]:
    razem = (mask["Age"] & mask[kol]).sum()
    print(f"Jednoczesne NaN w Age i {kol}: {razem}")
wynik = df.groupby(mask["Age"])["Survived"].agg(["count", "mean"])
wynik.index = ["Age obecny", "Age brak"]
wynik["mean"] *= 100
print("\nPrzeżycie w zależności od braków Age (%):\n", wynik.round(2))
print("\nWniosek: porównaj wspólne braki i wskaźniki przeżycia; współwystępowanie nie dowodzi przyczynowości.")
