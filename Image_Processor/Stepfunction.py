import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 7, 0.4)
y0 = np.sin(x)
y = y0.copy() + 2.5

plt.step(x, y, label='pre (default)')
z = np.heaviside([-1.5, 0, 2.0], 0.5)

plt.legend()

plt.xlim(0, 7)
plt.ylim(-0.5, 4)

plt.show()

