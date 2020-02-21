#pragma once
#include <tuple>


class Uniform_Texture : Texture_Material
{
    public:
        std::tuple<float, float> properties(Point3 pos)
        {
            pos = pos;
            return std::make_tuple(0.5, 0.5);
        }
};
