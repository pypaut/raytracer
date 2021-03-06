#pragma once
#include <cmath>


class Sphere : Object
{
    public:
        Sphere(Point3 center, float r)
        {
            center_ = center;
            r_ = r;
        }

        /* ** Proof **
        **
        ** Line :
        ** x(t) = vect_x * t + pt_x
        ** y(t) = vect_y * t + pt_y
        ** z(t) = vect_z * t + pt_z
        **
        ** Sphere :
        ** (x - c_x)**2 + (y - c_y)**2 + (z - c_z)**2 = r**2
        **
        ** We get a 2nd degree polynom with substitution method,
        ** and the answer we seek depends on the discriminant's sign.
        **
        ** It is important to note that a, b and c described below
        ** are not the exact coefficients of the polynom (factorized version).
        */
        bool intersects(Point3 pt, Vector3 vect)
        {
            float b = vect.get_x() * (pt.get_x() - center_.get_x())
                        + vect.get_y() * (pt.get_y() - center_.get_y())
                        + vect.get_z() * (pt.get_z() - center_.get_z());
            float b2 = pow(b, 2);

            float a = pow(vect.get_x(), 2)
                        + pow(vect.get_y(), 2)
                        + pow(vect.get_z(), 2);

            float c = pow(pt.get_x() - center_.get_x(), 2)
                    + pow(pt.get_y() - center_.get_y(), 2)
                    + pow(pt.get_z() - center_.get_z(), 2)
                    - pow(r_, 2);

            float delta = 4 * (b2 - a * c);

            return delta >= 0;
        }

        Vector3 normal(Point3 pt)
        {
            pt = pt;
            return Vector3(0, 0, 0);
        }

        Texture_Material getMaterial(Point3 pt)
        {
            pt = pt;
            return Texture_Material();
        }

    private:
        Point3 center_;
        float r_;
};
