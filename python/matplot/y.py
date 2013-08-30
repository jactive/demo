import numpy as np
import matplotlib.pyplot as plt

e = np.e
X, Y = np.meshgrid(np.linspace(0, 5, 100), np.linspace(0, 5, 100))
F = X ** Y
G = Y ** X

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.contour(X, Y, (F - G), [0])
plt.plot([e], [e], 'g.', markersize=20.0)
plt.draw()
plt.savefig("/tmp/pyplot/node.png")


