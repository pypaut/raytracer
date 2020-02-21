from Camera import Camera
from Image import Image
from Point3 import Point3
from PointLight import PointLight
from Raytracer import Raytracer
from Scene import Scene
from Sphere import Sphere
from Vector3 import Vector3


def main():
    W = 600
    H = 600

    s1 = Sphere()
    l1 = PointLight(0, 0, 5)

    camPos = Point3(5, 0, 0)
    camFwd = Vector3(-1, 0, 0)
    camUp = Vector3(0, 0, 1)
    camRf_x = 1
    camRf_y = 1
    camZ_min = 1
    cam = Camera(camPos, camFwd, camUp, camRf_x, camRf_y, camZ_min)

    scene = Scene([s1], [l1], cam)
    im = Raytracer.buildImage(scene, W, H)


if __name__ == "__main__":
    main()
