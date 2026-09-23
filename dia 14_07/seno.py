import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 300)

seno = pd.Series(np.sin(x), index=x)

seno.plot(linewidth=3, linestyle='dotted', color='green')

plt.title("Funcion Seno entre -pi y pi")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
