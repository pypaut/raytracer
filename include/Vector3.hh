#pragma once

class Vector3
{
    public:
        Vector3(float x, float y, float z);
        ~Vector3();

        float get_x();
        float get_y();
        float get_z();

        Vector3 operator*(const float &l) const;
        Vector3 operator+(const Vector3 &v) const;


    private:
        float x_;
        float y_;
        float z_;
};
