from Light import Light
from Vector3 import Vector3


class PointLight(Light):
    def __init__(self, x=0, y=0, z=0, i=1):
        """
        Point3 pos : position
        """
        self.pos = Vector3(x, y, z)
        self.i = i

    def intensity(self, pos):
        """
        Return the light's intensity as seen from pos.
        """
        # dist = Vector3.buildDir(self.pos, pos).norm()
        # return self.i / dist
        return self.i
