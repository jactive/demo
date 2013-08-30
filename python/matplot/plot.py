import numpy as np
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
matplotlib.pyplot.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat = np.random.rand(1000, 4);
ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
plt.draw()
plt.savefig("/tmp/pyplot/points.png")

