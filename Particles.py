import numpy
class Particles:
    def __int__(self, positions: numpy.narray, charges: numpy.array, masses: numpy.array):
        self.positions = positions
        self.charges =  charges
        self.masses = masses
    def size(self) -> int:
        return len(self.positions)
    def at(self, index : int) -> ((int, int, int), int, int): #position, charge, mass
        return (self.positions[index], self.charges[index], self.masses[index])
    def update(self, index: int, x: int, y: int, z: int) -> bool:
        if(index >= len(self.positions)):
            return False
        self.positions[index] = numpy.asarray([x, y, x])
        return True
