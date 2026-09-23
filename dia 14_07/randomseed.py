import pandas as pd
import numpy as np

np.random.seed(0)

r = np.random.random(size=6)

s=pd.Series(r)

print(s)