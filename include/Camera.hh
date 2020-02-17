#pragma once

#include "Point3.hh"
#include "Vector3.hh"


class Camera
{
    public:
        Camera(Point3 center,
                Vector3 forward,
                Vector3 upward,
                float read_field_x,
                float read_field_y,
                float z_min)
        {
            center_ = center;
            forward_ = forward;
            upward_ = upward;
            read_field_x_ = read_field_x;
            read_field_y_ = read_field_y_;
            z_min_ = z_min;
        }

        ~Camera()
        {
            delete center_;
            delete forward_;
            delete upward_;
            delete this;
        }

    private:
        Point3 center_;
        Vector3 forward_;
        Vector3 upward_;
        float read_field_x_;
        float read_field_y_;
        float z_min_;

};
