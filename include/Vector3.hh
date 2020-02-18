#pragma once


class Vector3
{
    public:
        Vector3()
        {
            x_ = 0;
            y_ = 0;
            z_ = 0;
        }

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

        float get_x() const
        {
            return x_;
        }

        float get_y() const
        {
            return y_;
        }

        float get_z() const
        {
            return z_;
        }

        Vector3 operator*(const float &l) const
        {
            float x = x_ * l;
            float y = y_ * l;
            float z = y_ * l;

            return Vector3(x, y, z);
        }

        Vector3 operator+(const Vector3 &v) const
        {
            float x = x_ + v.get_x();
            float y = y_ + v.get_y();
            float z = z_ + v.get_z();

            return Vector3(x, y, z);
        }

        Vector3 operator-(const Vector3 &v) const
        {
            float x = x_ - v.get_x();
            float y = y_ - v.get_y();
            float z = z_ - v.get_z();

            return Vector3(x, y, z);
        }

        std::ostream& operator<<(std::ostream &out)
        {
            return out
                << "Vector3("
                << x_
                << ", "
                << y_
                << ", "
                << z_
                << ")";
        }

    private:
        float x_;
        float y_;
        float z_;
};
