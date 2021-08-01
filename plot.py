import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('positions.tsv',delimiter='\t',skiprows=2)
time = data[:,0]
kinetic_energy = data[:,1]
average_velocity = data[:,2]
stdev_velocity = data[:,3]
piston_position = data[:,4]
particle_positions = data[:,5:]

fig, ax = plt.subplots(1,2)
ax[0].plot(time,piston_position)
for i in range(particle_positions.shape[1]):
    ax[0].plot(time,particle_positions[:,i],alpha=0.1)
ax[0].set_xlabel('time')
ax[0].set_ylabel('position')

ax[1].plot(time,stdev_velocity)
ax[1].set_xlabel('time')
ax[1].set_ylabel('Stdev Velocity')

plt.show()
