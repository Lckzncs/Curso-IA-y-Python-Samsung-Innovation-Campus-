import pandas as pd
import matplotlib.pyplot as plt 


rank = pd.read_json('universities_ranking.json')

index_position = rank.iloc[1:10]

#print(index_position)


df = index_position.copy()

df.rename(index={1:'a', 2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}, inplace=True)

index_label = df.loc[['a','b']]

print(index_label)