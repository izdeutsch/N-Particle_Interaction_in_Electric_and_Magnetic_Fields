Description of each file:

Camera.py--creates a Camera class in which the camera's position is setup, as well as updating particles and rendering them

Particles.py--creates a Particles class that stores positions, charges, and masses of particles

Particles_test.py--ignore in grading, just testing the functionality of the Particles class

Simulator.py--creates a class that calls the camera and sets up the start of the animation

animation_test.py--ignore in grading, testing animation ability

input.txt--text file where users can input initial conditions in the following format:
1 mass1,mass2,...
2 charge1,charge2,...
3 pos1_x,pos1_y,pos1_z,pos2_x,pos2_y,pos2_z...
4 vel1_x,vel1_y,vel1_z,vel2_x,vel2_y,vel2_z...
5 [((0,0,0),(0,0,-1),(0,1,0))] # camera positioning
6 lambda x,y,z:(E_x,E_y,E_z,B_x,B_y,B_z)

particle_simulation.py--contains all of the calculation aspects of the project (obtaining and updating E/B fields and particle positions)

particle_simulation_test.py--ignore in grading, just testing that the calculations in particle_simulation work the way they should in solve_ivp

user_inputs.py--final file (this is the one to run and animate) with the option of inputs coming from the terminal or from input.txt
