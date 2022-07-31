from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sys import argv


def get_freqs(img_pixels):
    freqs = [0 for _ in range(256)]
    for row in img_pixels:
        for intensity in row:
            freqs[intensity] += 1
    return freqs


def get_cumulative_freqs(freqs):
    cumulative_freqs = [0 for _ in range(256)]
    len_freqs = len(freqs)

    cumulative_freqs[0] = freqs[0]

    for index in range(1, len_freqs):
        cumulative_freqs[index] = cumulative_freqs[index - 1] + freqs[index]

    return cumulative_freqs


def get_normalized_freqs(freqs, size):
    normalized_freqs = [0 for _ in range(256)]
    index = range(256)
    for index in range(len(normalized_freqs)):
        normalized_freqs[index] = freqs[index] / size

    return normalized_freqs


def main():
    filename = argv[1]
    name = filename.split(".")[0]
    img = Image.open(filename)
    img_pixels = np.asarray(img)
    freqs = get_freqs(img_pixels)
    cumulative_freqs = get_cumulative_freqs(freqs)
    normalized_freqs = get_normalized_freqs(freqs, (img.size[0] * img.size[1]))

    plt.hist(
        range(256),
        weights=freqs,
        bins=256,
        alpha=1,
        color="#8caaee",
    )
    plt.title("Histograma da Frequência Absoluta")
    plt.xlabel("Intensidades")
    plt.ylabel("Frequência Absoluta")
    plt.axis([0, 256, 0, max(freqs) + min(freqs)])
    plt.savefig(f"imagens/Q2/fa-{name}.jpg")
    plt.clf()

    plt.hist(
        range(256),
        weights=cumulative_freqs,
        bins=256,
        alpha=1,
        color="#fa9e8c",
    )
    plt.title("Histograma da Frequência Acumulada")
    plt.xlabel("Intensidades")
    plt.ylabel("Frequência Acumulada")
    plt.axis([0, 256, 0, max(cumulative_freqs) + min(cumulative_freqs)])
    plt.savefig(f"imagens/Q2/faa-{name}.jpg")
    plt.clf()

    plt.hist(
        range(256),
        weights=normalized_freqs,
        bins=256,
        alpha=1,
        color="#a6d189",
    )
    plt.title("Histograma da Frequência Normalizada")
    plt.xlabel("Intensidades")
    plt.ylabel("Frequência Normalizada")
    plt.axis([0, 256, 0, max(normalized_freqs) + min(normalized_freqs)])
    plt.savefig(f"imagens/Q2/fn-{name}.jpg")


if __name__ == "__main__":
    main()
