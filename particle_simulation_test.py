from particle_simulation import get_fields2
from particle_simulation import COULOMBS_CONSTANT
from Particles import Particles
import numpy as np

def test1():
    print("test1:")
    positions = np.asarray([[0, 0, 0], [1, 2, 3]])
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

test1()
test2()