import numpy as np
import matplotlib.pyplot as plt
plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
plt.savefig("/tmp/pyplot/x.py.png")
