#pragma once

#include <Texture_Material.hh>

class Uniform_Texture : Texture_Material
{
    public:
        std::vector<int> properties(Point3 point);
};
