class Camera:
    def __init__(self, pos, fwd, up, rf_x, rf_y, z_min):
        """
        Point3   pos    : position
        Vector3  fwd    : forward vector
        Vector3  up     : upward vector
        float    rf_x   : reading field along x
        float    rf_y   : reading field along y
        float    z_min  : image plan distance to self
        """
        self.pos = pos
        self.fwd = fwd.normalized()
        self.up = up.normalized()
        self.right = self.fwd.cross(self.up).normalized()
        self.rf_x = rf_x
        self.rf_y = rf_y
        self.z_min = z_min
