import pandas as pd
import matplotlib.pyplot as plt

poblacion_2024 = {
    "Tokio": 14_000_000,
    "Pekin": 21_800_000,
    "Nueva Delhi": 33_800_000,
    "Moscu": 13_100_000,
    "Yakarta": 10_700_000,
    "Seul": 9_400_000,
    "Ciudad de Mexico": 9_200_000,
    "El Cairo": 10_100_000,
    "Londres": 8_900_000,
    "Paris": 2_100_000,
    "Madrid": 3_400_000,
    "Buenos Aires": 3_100_000,
    "Bangkok": 8_300_000,
    "Lima": 9_800_000,
    "Berlin": 3_800_000,
    "Roma": 2_750_000,
    "Ottawa": 1_020_000,
    "Washington D.C.": 680_000,
    "Brasilia": 2_900_000,
    "Santiago de Chile": 5_600_000,
}

poblacion_2025 = {
    "Tokio": 13_950_000,
    "Pekin": 21_900_000,
    "Nueva Delhi": 34_700_000,
    "Moscu": 13_150_000,
    "Yakarta": 10_800_000,
    "Seul": 9_350_000,
    "Ciudad de Mexico": 9_250_000,
    "El Cairo": 10_400_000,
    "Londres": 9_000_000,
    "Paris": 2_090_000,
    "Madrid": 3_450_000,
    "Buenos Aires": 3_120_000,
    "Bangkok": 8_350_000,
    "Lima": 10_000_000,
    "Berlin": 3_850_000,
    "Roma": 2_760_000,
    "Ottawa": 1_040_000,
    "Washington D.C.": 690_000,
    "Brasilia": 2_950_000,
    "Santiago de Chile": 5_650_000,
}

superficie_km2 = {
    "Tokio": 2194,
    "Pekin": 16410,
    "Nueva Delhi": 1484,
    "Moscu": 2561,
    "Yakarta": 661,
    "Seul": 605,
    "Ciudad de Mexico": 1495,
    "El Cairo": 606,
    "Londres": 1572,
    "Paris": 105,
    "Madrid": 604,
    "Buenos Aires": 203,
    "Bangkok": 1569,
    "Lima": 2672,
    "Berlin": 891,
    "Roma": 1285,
    "Ottawa": 2790,
    "Washington D.C.": 177,
    "Brasilia": 5760,
    "Santiago de Chile": 837,
}

s2024 = pd.Series(poblacion_2024)
s2025 = pd.Series(poblacion_2025)
s_superficie = pd.Series(superficie_km2)

fluctuacion = s2025 - s2024

print("Fluctuacion de poblacion (2025 - 2024):")
print(fluctuacion)

plt.figure(figsize=(14, 6))
plt.bar(fluctuacion.index, fluctuacion.values, color='steelblue')
plt.xticks(rotation=45, ha='right')
plt.title("Fluctuacion de poblacion por ciudad (2025 - 2024)")
plt.xlabel("Ciudad")
plt.ylabel("Diferencia de habitantes")
plt.tight_layout()
plt.show()

densidad = s2025 / s_superficie

print("\nDensidad de poblacion (hab/km2):")
print(densidad)

ciudad_max = densidad.idxmax()
ciudad_min = densidad.idxmin()

print("\nCiudad con mayor densidad:", ciudad_max, "-", round(densidad[ciudad_max], 2), "hab/km2")
print("Ciudad con menor densidad:", ciudad_min, "-", round(densidad[ciudad_min], 2), "hab/km2")

plt.figure(figsize=(14, 6))
plt.bar(densidad.index, densidad.values, color='coral')
plt.xticks(rotation=45, ha='right')
plt.title("Densidad de poblacion por ciudad (hab/km2)")
plt.xlabel("Ciudad")
plt.ylabel("Habitantes por km2")
plt.tight_layout()
plt.show()