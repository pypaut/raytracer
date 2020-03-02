import math as m
from Vector3 import Vector3
from Image import Image


class Raytracer:
    @classmethod
    def computePixPos(self, i, j, pixSize, screenUpLeft, cam):
        pixPos = (
            screenUpLeft
            + cam.right.times(i * pixSize)
            - cam.up.times(j * pixSize)
        )
        pixPos += cam.right.times(pixSize / 2) - cam.up.times(pixSize / 2)
        return pixPos

    @classmethod
    def ptIsAfterScreen(self, pt, pixPos, cam):
        objDir = Vector3.buildDir(pixPos, pt)
        dir_cond = pt and cam.fwd.dot(objDir) >= 0
        pos_cond = cam.pos.dist(pt) >= cam.pos.dist(pixPos)
        return dir_cond and pos_cond

    @classmethod
    def applyDiffuseComp(self, color, diffuseComp):
        return (
            color[0] * diffuseComp,
            color[1] * diffuseComp,
            color[2] * diffuseComp,
        )

    @classmethod
    def computeDiffuse(self, obj, pt, lights):
        """
        IMPORTANT
        Everything normalized, ending up with a [0,1]
        coefficient. This will efficiently scale the
        rendered color.
        """
        diffuseComp = 0
        for light in lights:
            L = Vector3.buildDir(pt, light.pos).normalized()
            obj.k_d = 1  # TODO
            add = obj.k_d * obj.normal(pt).dot(L) * light.intensity(pt)
            if add < 0:
                add = 0
            diffuseComp += add
        return diffuseComp

    @classmethod
    def buildImage(self, scene, pixSize):
        # Compute needed parameters
        cam = scene.cam
        vecCamPos = Vector3(cam.pos.x, cam.pos.y, cam.pos.z)
        screenCenter = vecCamPos + cam.fwd.times(cam.z_min)

        height = 2 * cam.z_min * m.tan(cam.rf_y)
        width = 2 * cam.z_min * m.tan(cam.rf_x)

        screenUpLeft = (
            screenCenter
            + cam.up.times(height / 2)
            - cam.right.times(width / 2)
        )
        nbPixH = int(height // pixSize)
        nbPixW = int(width // pixSize)

        # Pixel matrix
        pixels = []

        for i in range(nbPixH):
            line = []
            for j in range(nbPixW):
                pixPos = self.computePixPos(i, j, pixSize, screenUpLeft, cam)
                rayDir = Vector3.buildDir(cam.pos, pixPos).normalized()
                color = (0, 0, 0)
                dist_min = -1
                for obj in scene.objects:
                    pt = obj.intersects(pixPos, rayDir)
                    if not pt:
                        continue
                    if self.ptIsAfterScreen(pt, pixPos, cam):
                        dist = pt.dist(pixPos)
                        if (
                            dist_min == -1 or dist < dist_min
                        ):  # This point is closer
                            dist_min = dist
                            color = obj.color
                            diffuseComp = self.computeDiffuse(
                                obj, pt, scene.lights
                            )
                            color = self.applyDiffuseComp(color, diffuseComp)

                color = (int(color[0]), int(color[1]), int(color[2]))
                line.append(color)
            pixels.append(line)

        return Image(nbPixW, nbPixH, pixels)
