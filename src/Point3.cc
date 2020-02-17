class Point3
{
    public:
        Point3()
        {
            x_ = 0;
            y_ = 0;
            z_ = 0;
        }

        Point3(float x, float y, float z)
        {
            x_ = x;
            y_ = y;
            z_ = z;
        }

        ~Point3()
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

        std::ostream& operator<<(std::ostream &out, Point3 &vect)
        {
            return std::cout
                << "Point3("
                << _x
                << ", "
                << _y
                << ", "
                << _z
                << ")";
        }

    private:
        float x_;
        float y_;
        float z_;
};
