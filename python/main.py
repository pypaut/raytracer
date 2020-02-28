from Camera import Camera
from Image import Image
from PointLight import PointLight
from Raytracer import Raytracer
from Scene import Scene
from Sphere import Sphere
from Vector3 import Vector3


def main():
    s1 = Sphere(Vector3(0, -0.5, 0.5), ray=1, color=(255, 0, 0))
    s2 = Sphere(Vector3(0, -0.5, -0.5), ray=1, color=(0, 255, 0))
    s3 = Sphere(Vector3(0, 0.5, 0), ray=1, color=(0, 0, 255))
    l1 = PointLight(0, 0, 5)

    camPos = Vector3(3, 0, 0)
    camFwd = Vector3(-1, 0, 0)
    camUp = Vector3(0, 0, 1)
    camRf_x = 1
    camRf_y = 1
    camZ_min = 1
    pixSize = 0.01
    cam = Camera(camPos, camFwd, camUp, camRf_x, camRf_y, camZ_min)

    scene = Scene([s1, s2, s3], [l1], cam)

    print("Building image...")
    im = Raytracer.buildImage(scene, pixSize)

    print("Exporting...")
    im.exportPPM("result.ppm")


if __name__ == "__main__":
    main()
