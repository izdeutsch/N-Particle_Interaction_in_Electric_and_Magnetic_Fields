from Camera import camera
import time
class Simulator:

    def __init__(self):
        self.steps = []
        self.p = [] #particles at the initial state
        self.vels = []
        self.extern_fields = lambda x, y, z: (0, 0, 0, 0, 0, 0)
        self.cameras = []
    def update(self, p: tuple[float, list[tuple[float, float, float]]]) -> None: #t, x, y, z
        self.steps.append(p)
    def animate(self)->None:
        for step in self.steps:
            for cam in self.cameras:
                cam.render()
                cam.update_particles(step[1])
            time.sleep(step[0])

    def put_cameras(self, lst_cameras: list[tuple[tuple[float, float, float],tuple[float, float, float],tuple[float, float, float]]]) -> bool:
        for cam in lst_cameras:
            if(len(cam) >= 3):
                position = cam[0]
                normal = cam[1]
                pos_x = cam[2]
                args = cam[3:]
                self.cameras.append(camera(position, normal, pos_x, self.p, *args))
            else:
                return False
        return True
    def run(self, max_t: float, f, output: list = None) -> bool:
        temp = f(max_t, self.p, self.vels, self.extern_fields, self.update)
        if(output != None):
            output.append(temp)
        return temp == None

    def setup(self, get_user_inputs) -> bool:
        return get_user_inputs(self)
