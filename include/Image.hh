#pragma once

#include <vector>


class Image
{
    public:
        Image(std::vector<ColorRGB> pixels, int W, int H);
        ~Image();

        void export_ppm();


    private:
        int W_;
        int H_;
        std::vector<ColorRGB> pixels_;
};
