from Particles import Particles
import numpy as np

def test1():
    print("test1:")
    positions = np.asarray([[0, 0, 0]])
    charge = np.asarray([1])
    mass = np.asarray([1])
    p = Particles(positions, charge, mass)
    assert p.at(0) == ((0, 0, 0), 1, 1)
    p.update(0, 1, 2, 3)
    assert p.at(0) == ((1, 2, 3), 1, 1)
    print("no error")

def test2():
    print("test2:")
    positions = np.asarray([[0, 0, 0], [1,2,3]])
    charge = np.asarray([1, -1])
    mass = np.asarray([1, 2])
    p = Particles(positions, charge, mass)
    assert p.at(0) == ((0, 0, 0), 1, 1)
    assert p.at(1) == ((1, 2, 3), -1, 2)
    p.update(0, 4, 5, 6)
    assert p.at(0) == ((4, 5, 6), 1, 1)
    assert p.at(1) == ((1, 2, 3), -1, 2)
    print("no error")


test1()
test2()