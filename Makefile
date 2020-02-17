all:
	g++ -Wall -Werror -Wextra -pedantic -std=c++17 -Iinclude src/main.cc src/ColorRGB.cc src/Image.cc src/Point3.cc src/Sphere.cc src/Uniform_Texture.cc src/Vector3.cc -o raytracer

clean:
	rm raytracer
