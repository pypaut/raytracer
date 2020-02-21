#pragma once


class ColorRGB
{
    public:
        ColorRGB()
        {
            R_ = 0;
            G_ = 0;
            B_ = 0;
        }

        ColorRGB(int R, int G, int B)
        {
            R_ = R;
            G_ = G;
            B_ = B;
        }

        ~ColorRGB()
        {
            delete this;
        }

        int get_R() const
        {
            return R_;
        }

        int get_G() const
        {
            return G_;
        }

        int get_B() const
        {
            return B_;
        }

        std::ostream& operator<<(std::ostream &out)
        {
            return out << "RGB["
                << R_
                << ", "
                << G_
                << ", "
                << B_
                << "]";
        }

    private:
        int R_;
        int G_;
        int B_;
};
