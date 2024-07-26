from particle_simulation import get_fields2
from particle_simulation import get_function
from particle_simulation import COULOMBS_CONSTANT
from Particles import Particles
import numpy as np

from scipy.integrate import solve_ivp

def test1():
    print("test1:")
    positions = np.asarray([[0, 0, 0], [0, 0, 100]])
    charge = np.asarray([1, -1])
    mass = np.asarray([1, 2])
    p = Particles(positions, charge, mass)
    for field in get_fields2(p):
        print("(", end= "")
        for i in field:
            print(i / COULOMBS_CONSTANT, end = " ")
        print(")")

def test2():
    print("test2:")
    positions = np.asarray([[0, 0, 0], [1, 1, 1],[1, 2, 3]])
    charge = np.asarray([1, -1, 2])
    mass = np.asarray([1, 2, 1])
    p = Particles(positions, charge, mass)
    for field in get_fields2(p):
        print("(", end= "")
        for i in field:
            print(i / COULOMBS_CONSTANT, end = " ")
        print(")")

def test_get_function1():
    print("test_get_function1:")
    positions = np.asarray([[0, 0, 0], [0, 0, 100]])
    charge = np.asarray([1, -1])
    mass = np.asarray([1, 2])
    p = Particles(positions, charge, mass)
    get_pos_vel = get_function(p, get_fields2)
    y0 = [0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0] # pos1, vel1, pos2, vel2
    answer = solve_ivp(get_pos_vel, y0=y0, method='RK45', t_span=[0, 1], rtol=1e-4, args=(lambda x, y, z : (0, 0, 0),))
    #print(len(answer.y[0]))

    #for i in answer.y:
       #print(i[5])

    for i in range (1,59):
        print(answer.y[i,5])

test1()
#test2()
test_get_function1()
