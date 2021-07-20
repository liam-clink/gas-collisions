import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('positions.tsv',delimiter='\t',skiprows=1)

plt.plot([0,100],[0,0])
plt.plot([0,100],[1,1])
for i in range(1,data.shape[1]):
    plt.plot(data[:,0],data[:,i])
plt.show()
