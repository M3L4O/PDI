import equalizacao as eq
from sys import argv
import numpy as np
from PIL import Image


def get_specification(mapping_input, mapping_base, pixels):
    mapping_specification = [0 for _ in range(256)]

    for index in range(len(mapping_input)):
        diff = [abs(element - mapping_input[index]) for element in mapping_base]
        mapping_specification[index] = diff.index(min(diff))

    width, height = pixels.shape

    for x in range(width):
        for y in range(height):
            pixels[x, y] = mapping_specification[pixels[x, y]]

    return pixels


def main():
    filename, ext = argv[1].split(".")
    pixels_input = np.asarray(Image.open(argv[1]).convert("L"))
    pixels_base = np.asarray(Image.open(argv[2]).convert("L"))
    px, mapping_input = eq.equalize(pixels_input.copy())
    px, mapping_base = eq.equalize(pixels_base.copy())

    new_pixels = get_specification(mapping_input, mapping_base, pixels_input.copy())
    img = Image.fromarray(new_pixels)
    img.save(f"imagens/Q5/{filename}-specified.{ext}")


if __name__ == "__main__":
    main()
