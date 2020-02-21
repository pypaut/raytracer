#include "include.hh"


int main(int argc, char *argv[])
{
    argc = argc;
    argv = argv;
    int W = 600;
    int H = 600;

    int pixels[600 * 600 * 3];
    std::vector<ColorRGB> pixels;

    for (int i = 0; i < W * H; ++i)
    {
        std::cout << "Color" << std::endl;
        ColorRGB color = ColorRGB(255, 255, 255);
        pixels.push_back(color);
    }

    return 0;
}
