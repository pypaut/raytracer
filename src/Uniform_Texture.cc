#include <Texture_Material.hh>

#include "include.hh"


class Uniform_Texture : Texture_Material
{
    public:
        std::tuple properties(Point3 point)
        {
            return std::make_tuple(0.5, 0.5);
        }
};
