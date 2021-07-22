import numpy as np

number = 100
positions = np.zeros(number)
velocities = np.zeros_like(positions)
mass = 1.
piston_mass = 1.e6
masses = mass*np.ones_like(positions)

duration = 100.
steps = 1000
times = np.linspace(0.,duration,steps)
dt = times[1]-times[0]

bounds = np.array([0.,1.])

# Initial conditions
uniform = np.random.default_rng().uniform(low=0.,high=1.,size=(number,))
velocities[uniform <= 0.5] = -0.5
velocities[uniform > 0.5] = 0.5
positions = np.random.default_rng().uniform(low=bounds[0],high=bounds[1],size=(number,))
piston_velocity = 0.

# Start with two hard walls in 1D
f = open("./positions.tsv",'w')
f.write('Time\t'+str(number)+' Positions\n')
for i in range(len(times)):
    positions += dt*velocities

    # Reflect particles out of bounds
    past_piston_tuples = []
    for j in range(len(positions)):
        if positions[j] >= bounds[1]:
            offset_time = (positions[j]-bounds[1])/velocities[j]
            past_piston_tuples.append((j,offset_time))
        elif positions[j] <= bounds[0]:
            extra_distance = positions[j]-bounds[0]
            positions[j] = bounds[0]-extra_distance
            velocities[j] *= -1.
            
    # If out of bounds, sort and reflect sequentially
    if len(past_piston_tuples):
        past_piston_tuples.sort(key=lambda tup: tup[1])
        past_piston_tuples = past_piston_tuples[::-1]
        print(len(past_piston_tuples))
        for j in range(len(past_piston_tuples)):
            index = past_piston_tuples[j][0]
            extra_distance = positions[index]-bounds[1]
            positions[index] = bounds[1]-extra_distance
            velocity_change = 2*(-velocities[index] + piston_velocity)
            velocities[index] += velocity_change
            piston_velocity -= mass/piston_mass*(velocity_change)
    
    bounds[1] += dt*piston_velocity

    # Save state
    line = ''
    line += str(times[i]) + '\t'
    line += str(bounds[1])+'\t'
    for i in range(len(positions)):
        line += str(positions[i]) + '\t'
    line = line[:-1]+'\n'

    f.write(line)

f.close()