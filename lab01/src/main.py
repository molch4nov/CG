import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
a = int(input())
phi = np.arange(0, 2*np.pi, 0.01)
rho = a * (1 - np.cos(phi))
plt.plot(phi, rho, lw=1)
plt.show()