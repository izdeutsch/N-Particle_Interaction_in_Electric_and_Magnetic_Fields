import numpy
import Particles
import Camera
class Simulator:

    def __init__(self, ps: Particles, eField: numpy.narray, bField: numpy.narray):
        self.steps = []
        self.p = ps
        self.eField = eField
        self.bField = bField
        self.cameras = []
    def update(self, p: Particles, e: numpy.narray, b: numpy.narray) -> None:
        self.steps.append([p, e, b])
    def animate(self)->None:
        for step in self.steps:
            for camera in self.cameras:
                camera.particles = step[0]
                camera.set_visible(True)
                camera.render()
    def put_cameras(self, lst_cameras) -> bool:
        for camera in lst_cameras:
            if(len(camera) >= 3):
                position = camera[0]
                normal = camera[1]
                pos_x = camera[2]
                args = camera[3:]
                self.cameras.append(Camera(position, normal, pos_x, self.p, *args))
            else:
                return False
        return True
    def run(self, max_t: int, step_size: int, f, output: numpy.narray = None) -> bool:
        temp = f(max_t, step_size, self.update())
        if(output != None):
            output.append(temp)
        return temp == None

    def setup(self, get_user_inputs) -> bool:
        return get_user_inputs(self)
