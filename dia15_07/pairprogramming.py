import pandas as pd

df = pd.read_json('universities_ranking.json')

df['number students'] = pd.to_numeric(df['number students'].str.replace(',', ''), errors='coerce')
df['students staff ratio'] = pd.to_numeric(df['students staff ratio'], errors='coerce')
df['perc intl students'] = pd.to_numeric(df['perc intl students'].str.replace('%', ''), errors='coerce')

def extraer_ratio_femenino(v):
    if isinstance(v, str) and ':' in v:
        return float(v.split(':')[0])
    return float('nan')

df['female ratio (%)'] = df['gender ratio'].apply(extraer_ratio_femenino)

df = df.drop(columns=['gender ratio'])

print("Datos faltantes por columna:")
print(df.isnull().sum())

media = df['female ratio (%)'].mean()
df['female ratio (%)'] = df['female ratio (%)'].fillna(media)
print(f"\nfemale ratio (%) -> rellenado con la MEDIA: {media:.2f}")

mediana = df['perc intl students'].median()
df['perc intl students'] = df['perc intl students'].fillna(mediana)
print(f"perc intl students -> rellenado con la MEDIANA: {mediana:.2f}")

moda = df['location'].mode()[0]
df['location'] = df['location'].fillna(moda)
print(f"location -> se rellenaria con la MODA: '{moda}' (no tenia nulos)")

print("\nDatos faltantes tras limpieza:")
print(df.isnull().sum())