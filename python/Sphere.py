from Object import Object
from Vector3 import Vector3
import math as m


class Sphere(Object):
    def __init__(self, pos=Vector3(0, 0, 0), ray=1, color=(255, 255, 255)):
        self.pos = pos
        self.ray = ray
        self.color = color

    def __str__(self):
        return f"Sphere(Pos({self.pos}), Ray({self.ray}), Color({self.color}))"

    def intersects(self, rayPos, rayDir):
        """
        ** Proof **
        Line :
        x(t) = vect_x * t + pt_x
        y(t) = vect_y * t + pt_y
        z(t) = vect_z * t + pt_z

        Sphere :
        (x - c_x)**2 + (y - c_y)**2 + (z - c_z)**2 = r**2

        We get a 2nd degree polynom with substitution method,
        and the answer we seek depends on the discriminant's sign.

        Return the intersection point, if any.
        If there are two, we return the closest to pos.

        a, b and c are the same as in ax**2 + b*x + c = 0.
        """
        vec = Vector3.buildDir(self.pos, rayPos)

        a = rayDir.dot(rayDir)
        b = 2 * rayDir.dot(vec)
        c = vec.dot(vec) - self.ray**2

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            return None

        if delta == 0:  # Single solution
            t = -b / (2 * a)
            return rayDir.times(t) + rayPos

        # Two solutions
        t1 = (-b - m.sqrt(delta)) / (2 * a)
        t2 = (-b + m.sqrt(delta)) / (2 * a)

        pt1 = rayDir.times(t1) + rayPos
        pt2 = rayDir.times(t2) + rayPos


        if pt1.dist(rayPos) < pt2.dist(rayPos):
            return pt1
        return pt2

    def dist(self, vec):
        """
        Return the distance to a particular point.
        """
        v = Vector3(vec.x - self.pos.x, vec.y - self.pos.y, vec.z - self.pos.z)
        if v.norm() < self.ray:
            return 0
        return v.norm() - self.ray

    def normal(pos):
        """
        Return a normal vector to the surface of the sphere at
        the point position.
        """
        x = pos.x - self.pos.x
        y = pos.y - self.pos.y
        z = pos.z - self.pos.z
        return Vector(x, y, z).normalized()

    def getMaterial(pos):
        pos = pos
        return TextureMaterial()
