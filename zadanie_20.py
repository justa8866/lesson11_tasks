# Lekcja 11 - Zadanie 20
# Uruchom: python zadanie_20.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(URL)
full_kb = df.memory_usage(deep=True).sum() / 1024
selected = pd.read_csv(URL, usecols=["Name", "Age", "Sex", "Pclass", "Survived"])
selected_kb = selected.memory_usage(deep=True).sum() / 1024
# Szczytowe zużycie pojedynczego batcha (nie suma wszystkich batchy).
chunk_kb = max(chunk.memory_usage(deep=True).sum() / 1024 for chunk in pd.read_csv(URL, chunksize=100))
optimized = df.copy()
for kol in ["Pclass", "Survived", "SibSp", "Parch"]:
    optimized[kol] = optimized[kol].astype("int8")
for kol in ["Sex", "Embarked"]:
    optimized[kol] = optimized[kol].astype("category")
optimized_kb = optimized.memory_usage(deep=True).sum() / 1024
results = pd.DataFrame({
    "Metoda": ["Pełne wczytanie", "usecols (5 kolumn)", "chunksize=100 (maks. batch)", "Pełne + optymalizacja"],
    "Pamięć (KB)": [full_kb, selected_kb, chunk_kb, optimized_kb],
})
results["Oszczędność (%)"] = (1 - results["Pamięć (KB)"] / full_kb) * 100
# Założenie dydaktyczne: 1 MB RAM = 0.0003 kWh na godzinę.
results["Energia (kWh/h)"] = results["Pamięć (KB)"] / 1024 * 0.0003
results["Oszczędność energii (kWh/h)"] = (full_kb - results["Pamięć (KB)"]) / 1024 * 0.0003
print(results.round(6).to_string(index=False))
print("\nSłupki pamięci (█ = 10% pamięci wariantu pełnego):")
for _, row in results.iterrows():
    bar = "█" * round(row["Pamięć (KB)"] / full_kb * 10)
    print(f"{row['Metoda']:28s} |{bar:10s}| {row['Pamięć (KB)']:.2f} KB")
print("\nWniosek: usecols ogranicza liczbę kolumn, optymalizacja zmniejsza rozmiar typów,")
print("a chunksize ogranicza szczyt pamięci w trakcie przetwarzania.")
print("Energia to wyłącznie szacunek dydaktyczny, nie pomiar poboru prądu.")
