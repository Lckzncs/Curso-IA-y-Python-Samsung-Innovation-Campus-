import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset("titanic", cache = True)

#print(df.head())
#print(df.info())
#print(df["deck"].value_counts(dropna=False))
#print(df.isnull().sum())


df_sin_cubierta = df.dropna(axis=1, thresh=500)

#print(df_sin_cubierta.head())

df_con_edad = df_sin_cubierta.dropna(axis=0, how="any", subset=["age"])

#print(df_con_edad.head())
#print(len(df_con_edad))
#print(df_con_edad.isnull().sum())
sin_nans = df.dropna()
#print(sin_nans.isnull().sum())

#print (df['age'].head(10))

avg_age = df['age'].mean(axis=0)
#print(avg_age)

median_age = df['age'].median(axis=0)
#print(median_age)

df['age'] = df['age'].fillna(avg_age)
#print(df['age'].head(10))

#print(df.isnull().sum())

recuento_ciudades = df['embark_town'].value_counts()
#print(recuento_ciudades)
moda = recuento_ciudades.idxmax()
#print(moda)


df["embark_town"] = df["embark_town"].fillna(moda)
print(df.isnull().sum())

