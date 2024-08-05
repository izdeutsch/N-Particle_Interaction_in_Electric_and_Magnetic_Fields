from Simulator import Simulator
from Particles import Particles
import numpy as np
from particle_simulation import get_fields2
from particle_simulation import get_fields_collisions
from particle_simulation import get_function
from scipy.integrate import solve_ivp

def get_user_inputs(simulator: Simulator):
    ''' grabbing initial conditions based off of inputting into the terminal'''
    masses = [float(mass) for mass in input("Enter particle masses: ").split(",")]
    charges = [float(charge) for charge in input("Enter particle charges: ").split(",")]
    positions = [float(pos) for pos in input("Enter particle positions: ").split(",")]
    velocities = [float(vel) for vel in input("Enter particle velocities: ").split(",")]
    cam_setup = eval(input("Enter camera setups: "))
    ext_fields=eval(input("Enter external fields: "))
    #lambda x,y,z: (x**2, y*2, z, x, y, z)

    n = len(masses)
    assert len(charges) == n and len(positions) == n * 3 and len(positions) == len(velocities)

    pos_list=[]
    vel_list=[]
    i=0 
    while i<len(positions):
        pos_list.append([positions[i], positions[i+1], positions[i+2]])
        vel_list.append([velocities[i], velocities[i+1], velocities[i+2]])
        i+=3

    # putting the acquired information into use via the Particles class and into simulator:
    ps = Particles(np.asarray(pos_list), np.asarray(charges), np.asarray(masses))
    for s in ps:
        print(ps, 's')
    simulator.p = ps
    simulator.vels = vel_list
    simulator.extern_fields = ext_fields
    simulator.put_cameras(cam_setup)

def get_user_inputs2(simulator: Simulator, file: str = "input.txt"):
    '''obtaining initial conditions via file reading'''
    f = open(file, "r")
    masses = [float(mass) for mass in f.readline().split(",")]
    charges = [float(charge) for charge in f.readline().split(",")]
    positions = [float(pos) for pos in f.readline().split(",")]
    velocities = [float(vel) for vel in f.readline().split(",")]
    cam_setup = eval(f.readline())
    ext_fields=eval(f.readline())
    #lambda x,y,z: (x**2, y*2, z, x, y, z)

    n = len(masses)
    assert len(charges) == n and len(positions) == n * 3 and len(positions) == len(velocities)

    pos_list=[]
    vel_list=[]
    i=0
    while i<len(positions):
        pos_list.append([positions[i], positions[i+1], positions[i+2]])
        vel_list.append([velocities[i], velocities[i+1], velocities[i+2]])
        i+=3

    # putting the acquired information into use via the Particles class and into simulator:
    ps = Particles(np.asarray(pos_list), np.asarray(charges), np.asarray(masses))
    simulator.p = ps
    simulator.vels = vel_list
    simulator.extern_fields = ext_fields
    simulator.put_cameras(cam_setup)

def compute(max_t: float, particles: Particles, init_vels: list[tuple[float, float, float]], extern_fields, update):
    assert len(particles) == len(init_vels)
    get_pos_vel = get_function(particles, get_fields2) # grabbing positions, velocities
    y0 = []
    for i in range(len(particles)):
        currP = particles[i][0]
        currV = init_vels[i]
        # appending current positions and velocities to y0 (initial condiditon input into solve_ivp)
        y0.append(currP[0])
        y0.append(currP[1])
        y0.append(currP[2])
        y0.append(currV[0])
        y0.append(currV[1])
        y0.append(currV[2])
    print(y0)
    answer = solve_ivp(get_pos_vel, y0=y0, method='RK45', t_span=[0, max_t], rtol=1e-4,
                       args=(extern_fields,))
    n = len(answer.t)
    num_ps = len(particles)
    for i in range(n):
        lst = []
        t = answer.t[i]
        for j in range(num_ps):
            index = j * 6
            lst.append((answer.y[index][i], answer.y[index + 1][i], answer.y[index + 2][i]))
        update((t, lst))
    return answer

#just a test
sim = Simulator()
sim.setup(get_user_inputs2)
output = []
sim.run(10, compute, output)
#sim.animate()
#time_length=len(output[0].t)
#print(output[0].t[time_length-1])
#print(output[0].t[294])
#print(np.abs(-0.8208019600417122)) # collisions-get2 (get2 has t=221)
#print(output[0].t[242])

#get_user_inputs2(Simulator(), "input.txt")
