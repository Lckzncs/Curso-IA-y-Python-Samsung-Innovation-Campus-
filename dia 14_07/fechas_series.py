import pandas as pd
import numpy as np

np.random.seed(42)

fechas = pd.date_range(start='2025-01-04', end='2025-02-07')

s1 = pd.Series(np.random.uniform(2, 250, size=len(fechas)), index=fechas)
s2 = pd.Series(np.random.randint(7, 21, size=len(fechas)), index=fechas)
s3 = s1 / s2

print("Serie 1 - reales entre 2 y 250:")
print("Media:", s1.mean())
print("Mediana:", s1.median())
print("Maximo:", s1.max())
print("Minimo:", s1.min())

print("\nSerie 2 - enteros entre 7 y 20:")
print("Media:", s2.mean())
print("Mediana:", s2.median())
print("Maximo:", s2.max())
print("Minimo:", s2.min())

print("\nSerie 3 - s1 dividido s2:")
print("Media:", s3.mean())
print("Mediana:", s3.median())
print("Maximo:", s3.max())
print("Minimo:", s3.min())

sub_s1 = s1[s1.index < '2025-01-31']
print("\nSubserie de s1 antes del 31 de enero:")
print(sub_s1)
