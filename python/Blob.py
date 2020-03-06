from Object import Object
from Triangle import Triangle
from TriangleList import createTriangles
from Vector3 import Vector3


class Blob(Object):
    def __init__(
        self,
        pos,
        func,
        area,
        step,
        threashold,
        cam,
        color=(255, 255, 255),
        k_d=1,
        k_s=1,
        n_s=1,
    ):
        """
        pos : blob center
        func : decroissant function
        step : precision (cubes side)
        area : evaluated zone, which is an area^3 dimensioned matrix
        threashold : potential level we are looking for
        """
        self.pos = pos
        threashold = threashold
        self.color = color
        self.k_d = k_d
        self.k_s = k_s
        self.n_s = n_s

        x = cam.right
        y = cam.up.times(-1)
        z = cam.fwd

        # Marching cubes to create blob meshes
        self.meshes = []
        start_pt = self.pos + (y + x + z).times(-area / 2)
        nb_cubes = int(area // step)

        for x_i in range(nb_cubes):
            for y_i in range(nb_cubes):
                for z_i in range(nb_cubes):
                    # Cube vertices
                    v0 = start_pt + (
                        x.times(x_i * step)
                        + y.times(y_i * step)
                        + z.times(z_i * step)
                    )
                    v1 = v0 + x.times(step)
                    v2 = v1 + z.times(step)
                    v3 = v2 - x.times(step)
                    v4 = v0 + y.times(step)
                    v5 = v4 + x.times(step)
                    v6 = v5 + z.times(step)
                    v7 = v6 - x.times(step)

                    # Evaluate potentials
                    p0 = func(self.pos, v0)
                    p1 = func(self.pos, v1)
                    p2 = func(self.pos, v2)
                    p3 = func(self.pos, v3)
                    p4 = func(self.pos, v4)
                    p5 = func(self.pos, v5)
                    p6 = func(self.pos, v6)
                    p7 = func(self.pos, v7)
                    # print(p0, p1, p2, p3)

                    index = 0
                    if p0 < threashold:
                        index += 1
                    if p2 < threashold:
                        index += 2
                    if p1 < threashold:
                        index += 4
                    if p0 < threashold:
                        index += 8
                    if p7 < threashold:
                        index += 16
                    if p6 < threashold:
                        index += 32
                    if p5 < threashold:
                        index += 64
                    if p4 < threashold:
                        index += 128

                    self.meshes += createTriangles(
                        [v0, v1, v2, v3, v4, v5, v6, v7], index
                    )

    def intersects(self, rayPt, rayDir):
        for mesh in self.meshes:
            pt = mesh.intersects(rayPt, rayDir)
            if pt:
                return pt

    def normal(self, pt):
        normals = [mesh.normal(pt) for mesh in self.meshes]
        x = [n.x for n in normals]
        y = [n.y for n in normals]
        z = [n.z for n in normals]
        return Vector3(
            sum(x) / len(x), sum(y) / len(y), sum(z) / len(z)
        ).normalized()
