# Lekcja 11 - Zadanie 17
# Uruchom: python zadanie_17.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
missing = df.isnull()
# Stałe kolumny (bez braków) mają niezdefiniowaną korelację: NaN.
matrix = missing.astype(int).corr()
print("Macierz korelacji braków:\n", matrix.round(2).to_string())
kolumny = missing.columns[missing.any()].tolist()
print("\nKolumny z brakami:", kolumny)
for i, a in enumerate(kolumny):
    for b in kolumny[i + 1:]:
        corr = matrix.loc[a, b]
        print(f"{a} / {b}: korelacja={corr:.3f}; wspólne braki={(missing[a] & missing[b]).sum()}")
        if pd.notna(corr):
            print("  Wniosek:", "dodatnia współzależność braków" if corr > 0 else "ujemna współzależność braków" if corr < 0 else "brak liniowej współzależności braków")
print("Korelacja nie dowodzi związku przyczynowego.")
