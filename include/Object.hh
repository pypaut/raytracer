#pragma once

#include "Texture_Material.hh"


class Object
{
    public:
        virtual bool intersects(Point3 point, Vector3 vect);
        virtual Vector3 normal(Point3 point);
        virtual Texture_Material getMaterial(Point3 point);
};
