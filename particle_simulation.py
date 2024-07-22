# source for figuring out ode: https://flothesof.github.io/charged-particle-trajectories-E-and-B-fields.html

# general imports:
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import scipy
from scipy.integrate import ode
from scipy.integrate import solve_ivp
from matplotlib import animation
from matplotlib.animation import FuncAnimation 
#-------------------------------------------------------------------------------------------------------------------------------------------
'''I think the best way to deal with many particles without a ton of indexing when it comes to choosing
which charge to multiple when, etc, it that we create a class for the particles that defines basically their charge, 
position, velocity, etc initially. We then run the simulation for particle in particles so that we can easily grab 
things from the particle class without getting confused about trying to do things like position[0] to get the first
row of positions because we want to generalize to N particles.'''

positions=[]
velocities=[]

'''eventually, evenything below will need to go in a for loop for each progressing time step'''
# first we need to get the fields at (x0, y0, z0, v0):

def get_fields(position, velocity, q): # position and velocity are (Nx3) matrices, q is a (Nx1) matrix (each row is a new particle)  
    
    # here we define what we want E and B to be (that we're externally setting up)
    E_ext=np.array(1, x^2+2, 2*y) # sample choice
    B_ext=np.array(z, 0, 3*x) # sample choice

    # we also need to consider the E fields being created by the other points
    k=8.99*(10**9) # N*m^2/C
    distance=_________ # distance between the 2 interacting points; use scipy.spatial.distance_matrix?
    E_points=k*q[1]/(distance**2) # figure out how to specify the q in this to be q of other charges, not the one we're tracking  

    return E_ext, E_points, B_ext # returns the fields at the start of the timestep (t0)

#-------------------------------------------------------------------------------------------------------------------------------------------
# now we need to use these "starter fields" to help us get the next set of positions and velocities at (x1, y1, z1, v1):
def find_pos_vel(velocity, mass): # input is the velocities @ t0 (beginning of step, and mass of the particle
    Fields=get_fields(position, velocity) # also need the fields that we get from the get_fields function (also at t0)
    Force_E_ext=q*Fields[0] # F=q*E
    Force_E_points=q*Fields[1] # multiplies the charge we're focusing on to the E field caused by the other charge (F=k*q_1*q_2/r^2)
    Force_B_ext=q*np.cross(velocity,Fields[2]) # F=q*(v×B)
    net_force=Force_E_ext+Force_E_points+Force_B_ext
    accel=net_force/mass
    return np.array(velocity[0], velocity[1], velocity[2], accel[0],accel[1], accel[2]) # returns v and a in all 3 dimensions at t0

#-------------------------------------------------------------------------------------------------------------------------------------------
# now to use the ode function to find the positions and velocities at t1 (end of step)
initial_state=(position, velocity) # positions and velocities at t0
wanted_times=(step[i-1], step[i]) # going from start of step to end of step (would need to update this at the end of each looping
answer=solve_ivp(find_pos_vel, y0=initial_state, method='RK45', t_span=wanted_times, rtol=1e-4) 
positions.append(answer[0])
velocities.append(answer[1])
# doing this for one single step (from i-1 (t0) to i(t1))

# we then would put this whole thing in a loop for every single step since after each step the positions/velocities change, which in turn 
# change the E and B fields


#-------------------------------------------------------------------------------------------------------------------------------------------
'''ALTERNATIVE METHOD: USING CROSS PRODUCTS'''
# note: this section is a lot messier than the first attempt

# get this to run with something other that cross
initial_state=[position, velocity] # user input

def get_fields(position, velocity):
    dB_dt=___
    externalE=(x**2)+y+2*z # input
    k=22
    q=1 # input
    dE_dt=curl((externalE)+(k*q/(r**2)))
    
    return np.array(dB_dt, dE_dt) # -dB/dt, dE/dt


def setup(B, E):
    B=np.matrix([B]) # user input
    E=np.matrix([E])

    def get_x_v(t, [position, velocity], q, m):
    
        fields=solve_ivp(get_fields, y0=initial_state, method='RK45', t_span=(wanted_times[0],wanted_times[-1]), t_eval=wanted_times, rtol=1e-4) # solving using SHO equation again, using RK45 method
        B=fields[:,0] # updated one
        E=fields[:,1] # updated one

       
        return velocity, acceleration
    return get_x_v
    
f=setup([1,2,3],[4,5,6]) # set initial B and E


solve_ivp(f, y0=initial_state, method='RK45', t_span=(0,100), rtol=1e-4) # solving using SHO equation again, using RK45 method