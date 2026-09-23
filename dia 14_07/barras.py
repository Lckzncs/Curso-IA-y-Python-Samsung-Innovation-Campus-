import pandas as pd
import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s = pd.Series(dias, index=meses)

plt.bar(s.index, s.values, color='magenta')

plt.title("Dias por mes del anio")
plt.xlabel("Mes")
plt.ylabel("Dias")
plt.show()
