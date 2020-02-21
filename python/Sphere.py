class Sphere(Object):
    def __init__(self, pos=Point3(0, 0, 0), ray=1):
        self.pos = pos
        self.ray = ray

    def intersects(self, pos, vec):
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

        It is important to note that a, b and c described below
        are not the exact coefficients of the polynom (factorized version).
        """
        b = vec.x * (pos.x - self.pos.x)
            + vec.y * (pos.y - self.pos.y)
            + vec.z * (pos.z - self.pos.z)

        a = vec.x**2 + vec.y**2 + vec.z**2

        c = (pos.x - self.pos.x)**2
            + (pos.y - self.pos.y)**2
            + (pos.z - self.pos.z)**2
            - self.ray**2

        delta = 4 * (b**2 - a * c)

        return delta >= 0

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
