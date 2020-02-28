import math as m


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Print overload.
        """
        return f"Vector3({self.x},{self.y},{self.z})"

    def __add__(self, vec):
        """
        Sum overload.
        """
        x = self.x + vec.x
        y = self.y + vec.y
        z = self.z + vec.z
        return Vector3(x, y, z)

    def __sub__(self, vec):
        """
        Substraction overload.
        """
        x = self.x - vec.x
        y = self.y - vec.y
        z = self.z - vec.z
        return Vector3(x, y, z)

    @classmethod
    def buildDir(self, pt1, pt2):
        return Vector3(pt2.x - pt1.x, pt2.y - pt1.y, pt2.z - pt1.z)

    def dot(self, vec):
        """
        Dot product.
        """
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def cross(self, vec):
        """
        Cross product.
        """
        x = self.y * vec.z - self.z * vec.y
        y = self.z * vec.x - self.x * vec.z
        z = self.x * vec.y - self.y * vec.x
        return Vector3(x, y, z)

    def times(self, t):
        """
        Product with a scalar.
        """
        x = t * self.x
        y = t * self.y
        z = t * self.z
        return Vector3(x, y, z)

    def norm(self):
        return m.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalized(self):
        return self.times(1 / self.norm())

    def dist(self, pt):
        vec = Vector3(self.x - pt.x, self.y - pt.y, self.z - pt.z)
        return vec.norm()
