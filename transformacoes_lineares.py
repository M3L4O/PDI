from PIL import Image
import numpy as np
import math
import argparse


def get_affine_transformation(img_pixels):
    width, height = img_pixels.shape

    for x in range(width):
        for y in range(height):
            new_intensity = img_pixels[x, y] = round(C * img_pixels[x, y] + B)
            if new_intensity > 255:
                new_intensity = 255
            img_pixels[x, y] = new_intensity

    return img_pixels


def get_logarithm_transformation(img_pixels):
    width, height = img_pixels.shape

    for x in range(width):
        for y in range(height):
            new_intensity = round(C * math.log2(img_pixels[x, y] + 1))
            if new_intensity > 255:
                new_intensity = 255
            img_pixels[x, y] = new_intensity

    return img_pixels


def get_gama_transformation(img_pixels):
    width, height = img_pixels.shape

    for x in range(width):
        for y in range(height):
            new_intensity = img_pixels[x, y] = round(C * img_pixels[x, y] ** B)
            if new_intensity > 255:
                new_intensity = 255
            img_pixels[x, y] = new_intensity

    return img_pixels


def main():
    img = Image.open(source)
    img_pixels = np.asarray(img)

    funcs = [
        get_affine_transformation,
        get_logarithm_transformation,
        get_gama_transformation,
    ]
    for func, required in zip(funcs, requireds):
        if required:
            new_pixels = func(img_pixels.copy())
            new_image = Image.fromarray(new_pixels)
            new_image.save(
                f"imagens/Q4/{source.split('.')[0]}-{func.__name__.split('_')[1]}-{C}-{B}.{source.split('.')[1]}"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transformações lineares.")
    parser.add_argument("-a", "--affine", action="store_true")
    parser.add_argument("-l", "--logarithm", action="store_true")
    parser.add_argument("-g", "--gamma", action="store_true")
    parser.add_argument("-s", "--source", type=str)
    parser.add_argument("-B", type=float)
    parser.add_argument("-C", type=float)
    args = vars(parser.parse_args())
    requireds = list(args.values())[:3]
    source, B, C = list(args.values())[3:]
    main()
