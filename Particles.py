import numpy
class Particles:
    def __init__(self, positions: numpy.array, charges: numpy.array, masses: numpy.array):
        self.positions = positions
        self.charges =  charges
        self.masses = masses
    def size(self) -> int:
        return len(self.positions)
    def at(self, index : int) -> ((float, float, float), float, float): #position, charge, mass
        return (tuple(self.positions[index]), self.charges[index], self.masses[index])
    def update(self, index: int, x: float, y: float, z: float) -> bool:
        if(index >= len(self.positions)):
            return False
        self.positions[index] = numpy.asarray([x, y, z])
        return True
    #iterator
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if(self.index < len(self.positions)):
            temp = self.index
            self.index += 1
            return self.at(temp)
        raise StopIteration

    #subscriptable
    def __getitem__(self, index):
        return self.at(index)

    def __setitem__(self, index: int, value: tuple[float, float, float]):
        self.update(index, *value)

    def __len__(self):
        return self.size()