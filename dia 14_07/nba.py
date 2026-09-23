import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('nba_players.xls')

top10 = df['college'].value_counts().head(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(top10.index, top10.values, color='steelblue', edgecolor='black')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.3,
             str(int(bar.get_height())),
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title('Top 10 Universidades con más jugadores NBA', fontsize=14, fontweight='bold')
plt.xlabel('Universidad', fontsize=12)
plt.ylabel('Número de jugadores', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()