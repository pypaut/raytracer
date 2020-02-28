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
        """
        a = rayDir.x ** 2 + rayDir.y ** 2 + rayDir.z ** 2

        b = 2 * (
            rayDir.x * (rayPos.x - self.rayPos.x)
            + rayDir.y * (rayPos.y - self.rayPos.y)
            + rayDir.z * (rayPos.z - self.rayPos.z)
        )

        c = (
            (rayPos.x - self.rayPos.x) ** 2
            + (rayPos.y - self.rayPos.y) ** 2
            + (rayPos.z - self.rayPos.z) ** 2
            - self.ray ** 2
        )

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            return None

        if delta == 0:  # Single solution
            t = -b / (2 * a)
            return Vector3(
                rayDir.x * t + rayPos.x,
                rayDir.y * t + rayPos.y,
                rayDir.z * t + rayPos.z,
            )

        # Two solutions
        t1 = (-b - m.sqrt(delta)) / (2 * a)
        t2 = (-b + m.sqrt(delta)) / (2 * a)

        pt1 = Vector3(
            rayDir.x * t1 + rayPos.x,
            rayDir.y * t1 + rayPos.y,
            rayDir.z * t1 + rayPos.z,
        )

        pt2 = Vector3(
            rayDir.x * t2 + rayPos.x,
            rayDir.y * t2 + rayPos.y,
            rayDir.z * t2 + rayPos.z,
        )

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
