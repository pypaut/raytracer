from Light import Light
from Vector3 import Vector3


class PointLight(Light):
    def __init__(self, x=0, y=0, z=0):
        """
        Point3 pos : position
        """
        self.pos = Vector3(x, y, z)
