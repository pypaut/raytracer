#include "include.hh"


class ColorRGB
{
    public:
        ColorRGB(int R, int G, int B)
        {
            R_ = R;
            G_ = G;
            B_ = B;
        }

        ~ColorRGB();
        {
            delete this;
        }

        std::ostream& operator<<(std::ostream &out, ColorRGB &col)
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
