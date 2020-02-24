import math as m
from Vector3 import Vector3
from Image import Image


class Raytracer:
    @classmethod
    def buildImage(self, scene, pixSize):
        cam = scene.cam
        vecCamPos = Vector3(cam.pos.x, cam.pos.y, cam.pos.z)
        centerImageVec = vecCamPos + cam.fwd.times(cam.z_min)

        height = 2 * cam.z_min * m.tan(cam.rf_y)
        width = 2 * cam.z_min * m.tan(cam.rf_x)

        upperLeftImageVec = cam.up.times(height / 2) - cam.right.times(
            width / 2
        )
        nbPixH = int(height // pixSize)
        nbPixW = int(width // pixSize)

        print(cam.up)
        print(cam.right)
        print(cam.fwd)

        # Pixels
        pixels = []

        for i in range(nbPixH):
            line = []
            for j in range(nbPixW):
                color = (0, 0, 0)
                dist_min = -1
                for obj in scene.objects:
                    pixPos = (
                        upperLeftImageVec
                        + cam.right.times(i * pixSize)
                        - cam.up.times(j * pixSize)
                    )
                    # Aim at center of pixel
                    pixPos += cam.right.times(pixSize / 2) - cam.up.times(
                        pixSize / 2
                    )
                    rayDir = Vector3(
                        pixPos.x - cam.pos.x,
                        pixPos.y - cam.pos.y,
                        pixPos.z - cam.pos.z,
                    )
                    cond = rayDir.dot(cam.fwd) >= 0
                    pt = obj.intersects(cam.pos, rayDir)
                    if pt and cond:
                        dist = pt.dist(pixPos)
                        if dist_min == -1 or dist <= dist_min:
                            dist_min = dist
                            color = obj.color

                line.append(color)

            pixels.append(line)

        return Image(nbPixW, nbPixH, pixels)
