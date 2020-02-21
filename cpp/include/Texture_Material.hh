#pragma once


class Texture_Material
{
    public:
        virtual std::tuple<float, float> properties(Point3 point);
};
