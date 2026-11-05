# Lekcja 11 - Zadanie 1
# Uruchom: python zadanie_01.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

produkty = pd.DataFrame({
    "Nazwa": ["Laptop", "Mysz", "Monitor", "Klawiatura", "Drukarka", "Kabel", "Dysk", "Router", "Kamera", "Słuchawki"],
    "Cena": [3500, 70, 900, 150, 650, 30, 420, 210, 260, 180],
    "Ilość": [4, 25, 8, 12, 5, 80, 10, 9, 7, 16],
    "Kategoria": ["Komputery", "Akcesoria", "Monitory", "Akcesoria", "Druk", "Akcesoria", "Pamięć", "Sieć", "Wideo", "Audio"],
})
print("Pierwsze 5 produktów:\n", produkty.head())
produkty["WartośćCałkowita"] = produkty["Cena"] * produkty["Ilość"]
print("\nWszystkie produkty:\n", produkty.to_string(index=False))
print("\nŁączna wartość magazynu:", produkty["WartośćCałkowita"].sum(), "zł")
