#pragma once


class Sphere : Object
{
    public:
        Sphere(Point3 center, float r);
        bool intersects(Point3 pt, Vector3 vect);
        Vector3 normal(Point3 point);
        Texture_Material getMaterial(Point3 point);

    private:
        Point3 c_;
        float r_;
};
