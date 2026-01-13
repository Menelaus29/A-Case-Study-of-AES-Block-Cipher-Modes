from PIL import Image

def main():
    width, height = 256, 256
    block = 32

    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            if ((x // block) + (y // block)) % 2 == 0:
                pixels[x, y] = (255, 255, 255)  # white
            else:
                pixels[x, y] = (0, 0, 0)        # black

    img.save("data/pattern.png")
    print("pattern.png generated in data/ directory")

if __name__ == "__main__":
    main()
