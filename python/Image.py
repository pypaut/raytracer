class Image:
    def __init__(self, W, H, pixels):
        """
        Integer W      : width
        Integer H      : height
        List    pixels : H * W matrix of 3-uplets
        """
        self.W = W
        self.H = H
        self.pixels = pixels

    def __str__(self):
        s = ""
        for line in self.pixels:
            for e in line:
                s += f"{e} "
            s += "\n"
        return s

    def export_ppm(self, filename):
        """
        Export the Image as .ppm file.
        Will overwrite <filename> with the generated file.
        """
        file = open(filename, "w")

        # File header
        header = f"P3\n {self.W} {self.H}\n255\n"

        # Pixels
        pix = ""
        for i in range(self.H):
            for j in range(self.W):
                # Zero padding
                s_R = f"{self.pixels[i][j][0]:03}"
                s_G = f"{self.pixels[i][j][1]:03}"
                s_B = f"{self.pixels[i][j][2]:03}"
                pix += f"{s_R} {s_G} {s_B}   "
            pix += "\n"

        # Write
        text = header + pix
        file.write(text)

        file.close()
