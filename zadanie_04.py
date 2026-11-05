# Lekcja 11 - Zadanie 4
# Uruchom: python zadanie_04.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
wynik = df[(df["Age"] < 18) & (df["Survived"] == 1)]
print("Liczba ocalałych osób poniżej 18 lat:", len(wynik))
print(wynik[["Name", "Age"]].to_string(index=False))
