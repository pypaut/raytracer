from Image import Image

def main():
    W = 600
    H = 600
    pixels = []
    for i in range(W):
        line = []
        for j in range(H):
            line.append((0, 0, 0,))
        pixels.append(line)

    im = Image(W, H, pixels)
    im.export_ppm("TEST.ppm")

if __name__ == "__main__":
    main()
