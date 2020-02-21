#pragma once


class Scene
{
    private:
        std::vector<Object> objects_;
        std::vector<Light> lights_;
        Camera cam_;
};
