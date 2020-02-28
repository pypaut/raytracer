import math as m
from Vector3 import Vector3
from Image import Image


class Raytracer:
    @classmethod
    def buildImage(self, scene, pixSize):
        cam = scene.cam
        vecCamPos = Vector3(cam.pos.x, cam.pos.y, cam.pos.z)
        screenCenter = vecCamPos + cam.fwd.times(cam.z_min)

        height = 2 * cam.z_min * m.tan(cam.rf_y)
        width = 2 * cam.z_min * m.tan(cam.rf_x)

        screenUpLeft = screenCenter + cam.up.times(height / 2) - cam.right.times(
            width / 2
        )
        nbPixH = int(height // pixSize)
        nbPixW = int(width // pixSize)

        # Pixels
        pixels = []

        for i in range(nbPixH):
            line = []
            for j in range(nbPixW):
                color = (0, 0, 0)
                dist_min = -1
                pixPos = (
                    screenUpLeft
                    + cam.right.times(i * pixSize)
                    - cam.up.times(j * pixSize)
                )
                pixPos += cam.right.times(pixSize / 2) - cam.up.times(
                    pixSize / 2
                )
                rayDir = Vector3(
                    pixPos.x - cam.pos.x,
                    pixPos.y - cam.pos.y,
                    pixPos.z - cam.pos.z,
                )
                for obj in scene.objects:
                    pt = obj.intersects(cam.pos, rayDir)
                    if not pt:
                        continue
                    # Check if object is after the screen
                    dir_cond = pt and cam.fwd.dot(Vector3(pt.x, pt.y, pt.z)) <= 0 # ???
                    pos_cond = cam.pos.dist(pt) >= cam.pos.dist(pixPos)
                    if dir_cond and pos_cond:
                        dist = pt.dist(pixPos)
                        if dist_min == -1 or dist < dist_min:
                            dist_min = dist
                            color = obj.color

                line.append(color)
            pixels.append(line)

        return Image(nbPixW, nbPixH, pixels)
