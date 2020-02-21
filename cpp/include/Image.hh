#pragma once
#include <vector>
#include <fstream>
#include "ColorRGB.hh"


class Image
{
    public:
        Image(std::vector<ColorRGB> pixels, int W, int H)
        {
            pixels_ = pixels;
            W_ = W;
            H_ = H;
        }

        ~Image()
        {
            // delete pixels_;
            delete this;
        }

        int get_W()
        {
            return W_;
        }

        int get_H()
        {
            return H_;
        }

        std::vector<ColorRGB> get_pixels()
        {
            return pixels_;
        }

        std::ostream& operator<<(std::ostream &out)
        {
            int i = 0;

            for (auto it = pixels_.begin(); it != pixels_.end(); it++, i++) {
                std::string end = "";
                if (i > get_W()) {
                    end = ",\n";
                    i %= W_;
                }
                return out << "RGB["
                    << it->get_R()
                    << ", "
                    << it->get_G()
                    << ", "
                    << it->get_B()
                    << "] "
                    << end;
            }
        }

        void export_ppm(std::string filename)
        {
            // Open file
            std::ofstream myfile;
            myfile.open(filename);

            // File header
            myfile << "P3\n "
                << std::to_string(W_)
                << " "
                << std::to_string(H_)
                << "\n255\n";

            // Pixels
            int i = 0;
            for (auto it = pixels_.begin(); it != pixels_.end(); it++, i++) {
                std::string end = "";
                if (i > W_) {
                    end = "\n";
                    i %= W_;
                }

                // Zero padding
                std::string s_R = std::to_string(it->get_R());
                std::string s_G = std::to_string(it->get_G());
                std::string s_B = std::to_string(it->get_B());
                if (s_R.size() == 1) {
                    s_R = "00" + s_R;
                }
                else if (s_R.size() == 2) {
                    s_R = "0" + s_R;
                }
                if (s_G.size() == 1) {
                    s_G = "00" + s_G;
                }
                else if (s_G.size() == 2) {
                    s_G = "0" + s_G;
                }
                if (s_B.size() == 1) {
                    s_B = "00" + s_B;
                }
                else if (s_B.size() == 2) {
                    s_B = "0" + s_B;
                }

                // Writing
                myfile << s_R
                    << " "
                    << s_G
                    << " "
                    << s_B
                    << "   "
                    << end;
            }

            myfile.close();
        }

    private:
        int W_;
        int H_;
        std::vector<ColorRGB> pixels_;
};
