from Object import Object
from Vector3 import Vector3


class Triangle(Object):
    def __init__(self, v1, v2, v3, color=(255, 255, 255)):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.color = color

    def __str__(self):
        return f"Triangle({self.v1}, {self.v2}, {self.v3})"

    def normal(self, point):
        pt1_pt2 = Vector3(
            self.v2.x - self.v1.x, self.v2.y - self.v1.y, self.v2.z - self.v1.z
        )
        pt1_pt3 = Vector3(
            self.v3.x - self.v1.x, self.v3.y - self.v1.y, self.v3.z - self.v1.z
        )
        return pt1_pt2.cross(pt1_pt3).normalized()

    def intersects(self, rayPt, rayDir):
        """
        ** Proof **
        Line : rayPt + t * rayDir
        Plan : normal.dot(x) = d = - normal.dot(planPt)

        Merging the equasions gives :
        normal.dot(rayPt + t * rayDir) = - normal.dot(planPt)
        t = (-normal.dot(planPt) - normal.dot(rayPt)) / normal.dot(rayDir)
          = - normal.dot(planPt + rayPt) / normal.dot(rayDir)

        We can then check whether the intersection point is inside the triangle
        or not.
        """
        # Parallel
        normal = self.normal(rayPt)
        if normal.dot(rayDir) == 0:
            return None

        # Plan intersection
        planPt = self.v1
        t = -normal.dot(planPt + rayPt) / normal.dot(rayDir)
        interPoint = rayPt + rayDir.times(t)

        # Triangle intersection : inside-outside test
        e1 = self.v2 - self.v1
        vp1 = interPoint - self.v1
        c = e1.cross(vp1)
        if normal.dot(c) < 0:
            return None

        e2 = self.v3 - self.v2
        vp2 = interPoint - self.v2
        c = e2.cross(vp2)
        if normal.dot(c) < 0:
            return None

        e3 = self.v1 - self.v3
        vp3 = interPoint - self.v3
        c = e3.cross(vp3)
        if normal.dot(c) < 0:
            return None

        return interPoint

    def getMaterial(self, point):
        pass
