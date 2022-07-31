from PIL import Image
import numpy as np


def get_border_4(img_pixels):
    width, height = img_pixels.shape
    foreground = []
    for x in range(width):
        for y in range(height):
            if img_pixels[x, y] > 0 and (
                img_pixels[x + 1, y] > 0
                and img_pixels[x - 1, y] > 0
                and img_pixels[x, y + 1] > 0
                and img_pixels[x, y - 1] > 0
            ):
                foreground.append((x, y))

    for pixel in foreground:
        img_pixels[pixel] = 0

    return img_pixels


def get_border_8(img_pixels):
    width, height = img_pixels.shape
    foreground = []
    for x in range(width):
        for y in range(height):
            if img_pixels[x, y] > 0 and (
                img_pixels[x + 1, y] > 0
                and img_pixels[x + 1, y + 1] > 0
                and img_pixels[x + 1, y - 1] > 0
                and img_pixels[x - 1, y] > 0
                and img_pixels[x - 1, y + 1] > 0
                and img_pixels[x - 1, y - 1] > 0
                and img_pixels[x, y + 1] > 0
                and img_pixels[x, y - 1] > 0
            ):
                foreground.append((x, y))

    for pixel in foreground:
        img_pixels[pixel] = 0

    return img_pixels


def main():
    img = Image.open("folha.png").convert("L")
    img_pixels = np.asarray(img)

    new_pixels_4 = get_border_4(img_pixels.copy())
    new_img_4 = Image.fromarray(new_pixels_4)
    new_img_4.save("imagens/Q1/border-4.png")

    new_pixels_8 = get_border_8(img_pixels.copy())
    new_img_8 = Image.fromarray(new_pixels_8)
    new_img_8.save("imagens/Q1/border-8.png")

    diff_pixels_8_4 = new_pixels_8 - new_pixels_4
    new_img_diff = Image.fromarray(diff_pixels_8_4)
    new_img_diff.save("imagens/Q1/diff.png")


if __name__ == "__main__":
    main()
