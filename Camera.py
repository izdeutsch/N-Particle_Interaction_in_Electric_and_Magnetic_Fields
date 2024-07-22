import pyglet
from pyglet import shapes
class camera(pyglet.window.Window):
    key = pyglet.window.key
    # Indented oddly on purpose to show the pattern:
    UP = 0b0001
    DOWN = 0b0010
    LEFT = 0b0100
    RIGHT = 0b1000
    def __init__ (self, position, normal, pos_x, particles, radius = lambda x: 10, colorF = lambda x : (0, 0, 255) if x else (50, 225, 30), width=800, height=600, fps=False, *args, **kwargs):
        super(camera, self).__init__(width, height, *args, **kwargs)
        self.position = position
        self.normal = normal
        self.pos_x = pos_x
        self.pos_y = (normal[1] * pos_x[2] - normal[2] * pos_x[1], pos_x[0] * normal[2] - normal[0] * pos_x[2], normal[0] * pos_x[1] - normal[1] * pos_x[0])
        self.particles = particles
        self.colorF = colorF
        self.alive = 1
        self.circles = []

        for particle in particles:
            particle_position = particle.position
            particle_charge = particle.charge
            particle_mass = particle.mass
            vect = (position[0] - particle_position[0], position[1] - particle_position[1], position[2] - particle_position[2])
            dist = normal[0] * vect[0] + normal[1] * vect[1] + normal[2] * vect[2]
            point = (particle_position[0] - dist * normal[0], particle_position[1] - dist * normal[1], particle_position[2] - dist * normal[2])
            vect = (point[0] - position[0], point[1] - position[1], point[2] - position[2])
            x = pos_x[0] * vect[0] + pos_x[1] * vect[1] + pos_x[2] * vect[2]
            y = self.pos_y[0] * vect[0] + self.pos_y[1] * vect[1] + self.pos_y[2] * vect[2]
            self.circles.append(shapes.Circle(x, y, radius(particle_mass), color=self.colorF(particle_charge)))
    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == camera.key.ESCAPE: # [ESC]
            self.alive = 0

    def render(self):
        self.alive = 1
        self.clear()
        for circle in self.circles:
            circle.draw()
        ## Add stuff you want to render here.
        ## Preferably in the form of a batch.
        self.flip()
        self.dispatch_events()
