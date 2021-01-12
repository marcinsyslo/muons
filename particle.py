class Particle:
    def __init__(self, size, x, y, z):
        self.size = size
        self.cord = [x, y, z]

    def get_cord(self):
        return self.cord

    def set_cord(self, x, y, z):
        self.cord = [x, y, z]

    def get_size(self):
        return self.size

    def get_collision_range(self):
        return [self.cord[0]-self.size, self.cord[1]-self.size, self.cord[2]-self.size,
                self.cord[0]+self.size, self.cord[1]+self.size, self.cord[2]+self.size]
