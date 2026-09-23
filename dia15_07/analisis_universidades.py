import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('universities_ranking.json')

df['number students']      = pd.to_numeric(df['number students'].str.replace(',', ''), errors='coerce')
df['students staff ratio'] = pd.to_numeric(df['students staff ratio'], errors='coerce')
df['perc intl students']   = pd.to_numeric(df['perc intl students'].str.replace('%', ''), errors='coerce')
def extraer_ratio_femenino(v):
    if isinstance(v, str) and ':' in v:
        return float(v.split(':')[0])
    return float('nan')

df['female ratio (%)'] = df['gender ratio'].apply(extraer_ratio_femenino)

numericas = ['ranking', 'number students', 'students staff ratio',
             'perc intl students', 'female ratio (%)']

datos = df[numericas].copy()

print("Estadísticas básicas:")
print(datos.describe().round(2))

def linea_tendencia(xs, ys):
    n = len(xs)
    sum_x  = sum(xs)
    sum_y  = sum(ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys))
    sum_xx = sum(x * x for x in xs)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    return m, b

pares = [(a, b) for i, a in enumerate(numericas) for b in numericas[i+1:]]

fig, axes = plt.subplots(4, 3, figsize=(15, 18))
fig.suptitle('Gráficos de dispersión – Universidades', fontsize=14)

for i, (col_x, col_y) in enumerate(pares):
    ax = axes[i // 3][i % 3]
    sub = datos[[col_x, col_y]].dropna()
    xs = list(sub[col_x])
    ys = list(sub[col_y])
    ax.scatter(xs, ys, alpha=0.25, s=15, edgecolors='none')
    m, b = linea_tendencia(xs, ys)
    x_min, x_max = min(xs), max(xs)
    x_rango = [x_min + k * (x_max - x_min) / 99 for k in range(100)]
    ax.plot(x_rango, [m * x + b for x in x_rango], 'r--', linewidth=1.2)
    r = sub[col_x].corr(sub[col_y])
    ax.set_title(f'{col_x} vs {col_y}\nr = {r:.3f}', fontsize=8)
    ax.set_xlabel(col_x, fontsize=7)
    ax.set_ylabel(col_y, fontsize=7)
    ax.tick_params(labelsize=6)

for j in range(len(pares), 12):
    axes[j // 3][j % 3].set_visible(False)

plt.tight_layout()
plt.show()

corr = datos.corr()

print("\nMatriz de correlaciones:")
print(corr.round(3))

fig2, ax2 = plt.subplots(figsize=(7, 5))
im = ax2.imshow(corr.to_numpy(), cmap='RdYlGn', vmin=-1, vmax=1)

for i in range(len(corr)):
    for j in range(len(corr.columns)):
        ax2.text(j, i, f'{corr.iloc[i, j]:.2f}', ha='center', va='center', fontsize=9)

ax2.set_xticks(range(len(corr.columns)))
ax2.set_xticklabels(corr.columns, rotation=30, ha='right', fontsize=8)
ax2.set_yticks(range(len(corr.index)))
ax2.set_yticklabels(corr.index, fontsize=8)
fig2.colorbar(im, ax=ax2, label='Correlación de Pearson')
ax2.set_title('Mapa de calor de correlaciones – Universidades')

plt.tight_layout()
plt.show()

print("\n=== ANÁLISIS DE CORRELACIONES ===\n")

pares_corr = []
for i in range(len(corr)):
    for j in range(i + 1, len(corr.columns)):
        r = corr.iloc[i, j]
        pares_corr.append((abs(r), r, corr.index[i], corr.columns[j]))

pares_corr.sort(reverse=True)

for _, r, a, b in pares_corr:
    if abs(r) >= 0.5:
        fuerza = "fuerte"
    elif abs(r) >= 0.3:
        fuerza = "moderada"
    else:
        fuerza = "débil"
    sentido = "positiva" if r >= 0 else "negativa"
    print(f"  {a}  <->  {b}")
    print(f"    r = {r:.3f}  -> correlación {fuerza} {sentido}\n")