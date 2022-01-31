import matplotlib.pyplot as plt
import numpy as np

x = np.zeros(100)
for i in range (100):
    x[i] = np.sin(0.3*i)

plt.plot(x)
plt.show()