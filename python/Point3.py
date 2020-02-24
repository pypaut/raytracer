from Vector3 import Vector3


class Point3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point3({self.x},{self.y},{self.z})"

    def dist(self, pt):
        vec = Vector3(
            self.x - pt.x,
            self.y - pt.y,
            self.z - pt.z
        )
        return vec.norm()
