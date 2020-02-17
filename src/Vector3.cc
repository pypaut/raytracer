#include "include.hh"


class Vector3
{
    public:
        Vector3(float x, float y, float z)
        {
            x_ = x;
            y_ = y;
            z_ = z;
        }

        ~Vector3()
        {
            delete this;
        }

        float get_x()
        {
            return x_;
        }

        float get_y()
        {
            return y_;
        }

        float get_z()
        {
            return z_;
        }

        Vector3 operator*(const float &l) const
        {
            float x = get_x() * l;
            float y = get_y() * l;
            float z = get_z() * l;

            return new Vector3(x, y, z);
        }

        Vector3 operator+(const Vector3 &v) const
        {
            float x = get_v() + v.get_x();
            float y = get_v() + v.get_y();
            float z = get_v() + v.get_z();

            return new Vector3(x, y, z);
        }

        Vector3 operator−(const Vector3 &v) const
        {
            float x = get_v() - v.get_x();
            float y = get_v() - v.get_y();
            float z = get_v() - v.get_z();

            return new Vector3(x, y, z);
        }

        std::ostream& operator<<(std::ostream &out, Vector3 &vect)
        {
            return out
                << "Vector3("
                << vect.get_x()
                << ", "
                << vect.get_y()
                << ", "
                << vect.get_z()
                << ")";
        }

    private:
        float x_;
        float y_;
        float z_;
};
