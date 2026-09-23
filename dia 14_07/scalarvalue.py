import pandas as pd
import numpy as np

s = pd.Series([0, 1, 2, 3])

arr = np.arange(0,5)

ss = pd.Series(arr)

print(s)
print(ss)
print(s*ss)