# Lekcja 11 - Zadanie 5
# Uruchom: python zadanie_05.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
missing = df.isnull().sum()
percent = missing / len(df) * 100
raport = pd.DataFrame({"Liczba NaN": missing, "Procent NaN": percent})
print("Braki we wszystkich kolumnach:\n", raport.round(2))
print("\nKolumny z ponad 10% braków:\n", raport[raport["Procent NaN"] > 10].round(2))
