import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('positions.tsv',delimiter='\t',skiprows=1)
time = data[:,0]
piston_position = data[:,1]

plt.plot([0,100],[0,0])
plt.plot(time,piston_position)
for i in range(1,data.shape[1]):
    plt.plot(time,data[:,i],alpha=0.1)
plt.xlabel('time')
plt.ylabel('position')
plt.show()
