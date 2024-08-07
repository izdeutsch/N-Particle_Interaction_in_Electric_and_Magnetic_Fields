from Camera import camera
from particle_simulation import get_fields2
from particle_simulation import get_function
from particle_simulation import COULOMBS_CONSTANT
from Particles import Particles
import numpy as np
from scipy.integrate import solve_ivp
import time

def simple_test1():
    positions = np.asarray([[0, 0, 0], [0, 100, 0]])
    charge = np.asarray([1, -1])
    mass = np.asarray([1, 2])
    p = Particles(positions, charge, mass)
    c = camera((0, 0, 0), (0, 0, 1), (1, 0, 0), p)
    while(c.alive):
        c.render()

def simple_test2():
    positions = np.asarray([[0, 0, 0], [0, 100, 0]])
    charge = np.asarray([1, -1])
    mass = np.asarray([1, 2])
    p = Particles(positions, charge, mass)
    c1 = camera((0, 0, 0), (0, 0, 1), (1, 0, 0), p) # point the camera and then set orientation
    c2 = camera((0, 0, 0), (-1, 0, 0), (0, 1, 0), p)
    while(c1.alive and c2.alive):
        c1.render()
        time.sleep(1)
        c2.render()

def animation_test():
    positions = np.asarray([[0, 0, 0], [0, 0, 200]])
    charge = np.asarray([1, -1])
    mass = np.asarray([100000, 1000]) 
    p = Particles(positions, charge, mass)
    get_pos_vel = get_function(p, get_fields2)
    y0 = [0, 0, 0, 0, 0, 0, 0, 0, 200, 0, -271.65, 0]  # pos1, vel1, pos2, vel2
    answer = solve_ivp(get_pos_vel, y0=y0, method='RK45', t_span=[0, 1], rtol=1e-4,
                       args=(lambda x, y, z: (0, 0, 0, 0, 0, 0),))
    c = camera((0, 0, 0), (-1, 0, 0), (0, 1, 0), p, width= 1000, height= 700)
    y = answer.y
    length = len(y[0])
    print(length)
    print(answer.t)
    t = answer.t
    #count = 0
    for i in range(length):
        if(not c.alive):
            break
        c.render()
        time.sleep(t[i]/2) # speeding up the time between renderings
        c.update_particles([(y[0][i], y[1][i], y[2][i]), (y[6][i], y[7][i], y[8][i])])

#simple_test1()
#simple_test2()
animation_test()
