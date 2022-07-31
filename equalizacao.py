from PIL import Image
import numpy as np
import histograma
from sys import argv


def get_normalized_cumulative_freq(img_pixels):
    normalized_freq = histograma.get_normalized_freqs(
        histograma.get_freqs(img_pixels), img_pixels.size
    )
    normalized_cumulative_freq = [0 for _ in range(256)]

    normalized_cumulative_freq[0] = normalized_freq[0]

    for index in range(1, len(normalized_freq)):
        normalized_cumulative_freq[index] = (
            normalized_cumulative_freq[index - 1] + normalized_freq[index]
        )

    return normalized_cumulative_freq


def equalize(img_pixels):
    normalized_cumulative_freq = get_normalized_cumulative_freq(img_pixels)
    mapping = [
        round(255 * prob_cumulative) for prob_cumulative in normalized_cumulative_freq
    ]
    width, height = img_pixels.shape

    for y in range(height):
        for x in range(width):
            img_pixels[x, y] = mapping[img_pixels[x, y]]

    return img_pixels, mapping


def main():
    filename = argv[1]
    name, ext = filename.split(".")

    img = Image.open(filename).convert("L")
    img_pixels = np.asarray(img)

    new_pixels, mapping = equalize(img_pixels.copy())
    new_image = Image.fromarray(new_pixels)
    new_image.save(f"imagens/Q3/{name}-equalized.{ext}")


if __name__ == "__main__":
    main()
