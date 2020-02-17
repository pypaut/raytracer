#pragma once

#include <ostream>


class ColorRGB
{
    public:
        ColorRGB(int R, int G, int B);
        ~ColorRGB();


    private:
        int R_;
        int G_;
        int B_;
};
