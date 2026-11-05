# Lekcja 11 - Zadanie 19
# Uruchom: python zadanie_19.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
q1, q3 = df["Fare"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = (df["Fare"] < lower) | (df["Fare"] > upper)
print(f"Zakres IQR: [{lower:.2f}, {upper:.2f}]; outliery: {outliers.sum()}")
removed = df.loc[~outliers].copy()
capped = df.copy()
capped["Fare"] = np.clip(capped["Fare"], lower, upper)
logged = df.copy()
logged["Fare"] = np.log1p(logged["Fare"])
for nazwa, dane in [("Oryginał", df), ("Usunięcie", removed), ("Capping", capped), ("log1p", logged)]:
    print(f"\n{nazwa} - Fare:\n{dane['Fare'].describe()}")
    print(f"Skośność: {dane['Fare'].skew():.3f}")
wyniki = {"Usunięcie": abs(removed["Fare"].skew()), "Capping": abs(capped["Fare"].skew()), "log1p": abs(logged["Fare"].skew())}
print("\nNajbardziej symetryczny wg |skośności|:", min(wyniki, key=wyniki.get))
print("Uwaga: po log1p wartości Fare są w skali logarytmicznej, nie w GBP.")
