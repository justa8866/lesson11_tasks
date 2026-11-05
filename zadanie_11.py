# Lekcja 11 - Zadanie 11
# Uruchom: python zadanie_11.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
# Wiek brakujący pozostaje NaN - nie przypisujemy sztucznej grupy.
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, np.inf], labels=["0-12", "13-18", "19-35", "36-60", "60+"], include_lowest=True)
for kol in ["FamilySize", "IsAlone", "AgeGroup"]:
    print(f"\n{kol}:\n{df[kol].value_counts(dropna=False)}")
print("\nWskaźnik przeżycia wg IsAlone (%):\n", (df.groupby("IsAlone")["Survived"].mean() * 100).round(2))
