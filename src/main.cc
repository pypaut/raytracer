#include "include.hh"


int main(int argc, char *argv[])
{
    argc = argc;
    argv = argv;
    int W = 600;
    int H = 600;

    std::vector<ColorRGB> pixels;
    for (int i = 0; i < W * H; ++i)
    {
        pixels.push_back(ColorRGB(255, 255, 255));
    }

    return 0;
}
