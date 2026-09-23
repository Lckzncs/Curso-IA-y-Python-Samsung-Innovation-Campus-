import pandas as pd

#data={'col_1': [3, 2, 1, 0], 'col_2': ['a', 'D', 'c', 'd']}
#df = pd.DataFrame(data)
#print(df)


#s = pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c'])
#s2 = pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'])
#
#data={'one': s, 'two': s2}
#df = pd.DataFrame(data)
#print(df)

#d = {'col1': [1, 2], 'col2': [3, 4]}
#df = pd.DataFrame(data=d)

#print(df)

#df.index = ["new index0", "new index 1"]
#print(df)

#df.columns= ["new col1", "new col2"]
#print(df)

s = pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c'])
s2 = pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'])

data={'row_1': s, 'row_2': s2}
df = pd.DataFrame.from_dict(data, orient='index')
print(df)