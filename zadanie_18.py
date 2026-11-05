# Lekcja 11 - Zadanie 18
# Uruchom: python zadanie_18.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

def clean_titanic(df):
    clean = df.copy()
    clean = clean.loc[:, clean.isna().mean() <= 0.60].copy()
    if "Age" in clean:
        clean["Age"] = clean["Age"].fillna(clean["Age"].median())
    if "Embarked" in clean:
        moda = clean["Embarked"].mode(dropna=True)
        if not moda.empty:
            clean["Embarked"] = clean["Embarked"].fillna(moda.iloc[0])
    for kol in ["Pclass", "Survived", "SibSp", "Parch"]:
        if kol in clean and clean[kol].notna().all() and clean[kol].between(-128, 127).all():
            clean[kol] = clean[kol].astype("int8")
    for kol in ["Sex", "Embarked"]:
        if kol in clean:
            clean[kol] = clean[kol].astype("category")
    if {"SibSp", "Parch"}.issubset(clean.columns):
        clean["FamilySize"] = clean["SibSp"] + clean["Parch"] + 1
    return clean


titanic = pd.read_csv(URL)
original = titanic.copy(deep=True)
cleaned = clean_titanic(titanic)
print("Przed:", titanic.shape, "Po:", cleaned.shape)
cleaned.info()
print("\nBraki po czyszczeniu:\n", cleaned.isna().sum())
print("Oryginał bez zmian:", titanic.equals(original))
