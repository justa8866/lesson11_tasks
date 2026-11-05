# Lekcja 11 - Zadanie 15
# Uruchom: python zadanie_15.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

total_passengers = 0
age_sum = 0.0
age_count = 0
survived_sum = 0
for chunk in pd.read_csv(URL, chunksize=50):
    total_passengers += len(chunk)
    age_sum += chunk["Age"].sum()
    age_count += chunk["Age"].count()
    survived_sum += chunk["Survived"].sum()
stream = {"total_passengers": total_passengers, "avg_age": age_sum / age_count, "survival_rate": survived_sum / total_passengers * 100}
full = pd.read_csv(URL)
full_stats = {"total_passengers": len(full), "avg_age": full["Age"].mean(), "survival_rate": full["Survived"].mean() * 100}
print(pd.DataFrame({"Batch (50)": stream, "Cały plik": full_stats}).round(4))
print("Wyniki zgodne:", all(np.isclose(stream[k], full_stats[k]) for k in stream))
