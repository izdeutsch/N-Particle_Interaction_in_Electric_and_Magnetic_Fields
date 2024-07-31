#from Simulator import Simulator
#import Particles
#import Camera

def get_user_inputs():
    #masses = [float(mass) for mass in input("Enter particle masses: ").split(",")]
    #charges = [float(charge) for charge in input("Enter particle charges: ").split(",")]
    #positions = [float(pos) for pos in input("Enter particle positions: ").split(",")]
    #velocities = [float(vel) for vel in input("Enter particle velocities: ").split(",")]
    ext_fields=0
    exec('ext_fields=lambda x,y,z: (x**2, y*2, z)')
    #input("Enter external fields: ")

    print(type(ext_fields))
    #print(ext_fields(0,0,0))
    # x^2+y+2z, 4x+2z

    '''pos_list=[]
    vel_list=[]
    i=0 
    while i<len(positions):
        pos_list.append([positions[i], positions[i+1], positions[i+2]])
        vel_list.append([velocities[i], velocities[i+1], velocities[i+2]])
        i+=3'''

get_user_inputs()