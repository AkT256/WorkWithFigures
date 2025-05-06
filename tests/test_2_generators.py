# tests/test_2_generators.py
"""
Тест 2. Генераторы (пункт 2)
"""

import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from itertools import islice

from polygons_api.generators import gen_rectangle, gen_triangle, gen_hexagon


def demo():
    # П.2.1: генерируем по 7 фигур каждого типа
    rectangles = list(islice(gen_rectangle(dx=3), 7))
    triangles  = list(islice(gen_triangle(dx=3), 7))
    hexagons   = list(islice(gen_hexagon(dx=3), 7))

    # П.2.2: рисуем три подграфика в одной строке
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    datasets = [rectangles, triangles, hexagons]
    titles = ["Rectangles (7)", "Triangles (7)", "Hexagons (7)"]

    for ax, polys, title in zip(axes, datasets, titles):
        for poly in polys:
            xs, ys = zip(*poly)
            # добавляем первую точку в конец, чтобы замкнуть контур
            ax.plot(list(xs) + [xs[0]], list(ys) + [ys[0]])
        ax.set_aspect('equal')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()

