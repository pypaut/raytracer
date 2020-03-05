from Camera import Camera
from Image import Image
from PointLight import PointLight
from Raytracer import Raytracer
from Scene import Scene
from Sphere import Sphere
from Triangle import Triangle
from Vector3 import Vector3


def main():
    x = Vector3(1, 0, 0)
    y = Vector3(0, 1, 0)
    z = Vector3(0, 0, 1)

    s_floor = Sphere(
        Vector3(0, 50, 0), ray=50, color=(10, 10, 10), k_d=10, k_s=1, n_s=1
    )
    s_white = Sphere(Vector3(5, 0, 0), ray=3)
    s_red = Sphere(Vector3(0, -1, 0), ray=1, color=(255, 0, 0))
    s_green = Sphere(Vector3(0, -1, -5), ray=1, color=(0, 255, 0))
    s_blue = Sphere(Vector3(-5, -1, 0), ray=1, color=(0, 0, 255))
    t1 = Triangle(
        Vector3(20, 5, 10),
        Vector3(20, -10, 0),
        Vector3(20, 5, -10),
        color=(255, 255, 0),
        k_d=1,
        k_s=5,
        n_s=5,
    )

    l4 = PointLight(10, -10, 10)

    camPos = Vector3(10, -10, 0)
    camFwd = Vector3(-1, 1, 0)
    camUp = Vector3(0, 0, 1)
    camRf_x = 1
    camRf_y = 1
    camZ_min = 1
    pixSize = 0.01
    cam = Camera(camPos, camFwd, camUp, camRf_x, camRf_y, camZ_min)

    scene = Scene([s_floor, s_white, s_red, s_green, s_blue, t1], [l4], cam)

    print("Building image...")
    im = Raytracer.buildImage(scene, pixSize)

    print("Exporting...")
    im.exportPPM("result.ppm")


if __name__ == "__main__":
    main()
