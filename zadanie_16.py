# Lekcja 11 - Zadanie 16
# Uruchom: python zadanie_16.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["FamilyID"] = df["Name"].str.split(",").str[0].str.strip() + "_" + df["FamilySize"].astype(str)
rodziny = df[df["FamilySize"] > 1]
stat = rodziny.groupby("FamilyID")["Survived"].agg(["mean", "count", "sum"])
stat = stat[stat["mean"] >= 0.5].sort_values(["count", "mean"], ascending=False)
stat = stat.rename(columns={"mean": "Odsetek przeżycia", "count": "Liczba pasażerów", "sum": "Ocalało"})
stat["Odsetek przeżycia"] *= 100
print("Top 10 rodzin (nazwisko + FamilySize):\n", stat.head(10).round(2).to_string())
print("\nUwaga: FamilyID jest uproszczeniem; osoby o tym samym nazwisku i FamilySize nie muszą być jedną rodziną.")
