# Lekcja 11 - Zadanie 13
# Uruchom: python zadanie_13.py

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

daty = pd.date_range("2024-01-01", periods=20, freq="D")
wartosci = [10, 12, np.nan, np.nan, 18, 20, np.nan, 25, 27, np.nan, np.nan, np.nan, 35, 38, 40, np.nan, 45, 47, 50, np.nan]
df = pd.DataFrame({"Oryginał": wartosci}, index=daty)
df["ffill"] = df["Oryginał"].ffill()
df["bfill"] = df["Oryginał"].bfill()
df["linear"] = df["Oryginał"].interpolate(method="linear")
print("Porównanie metod:\n", df.round(2).to_string())
for kol in df.columns:
    print(f"\n{kol} (█ = 2 jednostki):")
    for data, wartosc in df[kol].items():
        slupek = "(NaN)" if pd.isna(wartosc) else "█" * max(0, int(wartosc // 2))
        print(f"{data.date()} | {slupek} {wartosc:.2f}")
print("\nffill używa poprzedniej wartości, bfill następnej, a linear interpoluje pomiędzy punktami.")
