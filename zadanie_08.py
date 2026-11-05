# Lekcja 11 - Zadanie 8
# Uruchom: python zadanie_08.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
wynik = df.query("Pclass == 1 and Fare > 50")
print("Liczba pasażerów:", len(wynik))
print(f"Średnia cena biletu: {wynik['Fare'].mean():.2f} GBP")
