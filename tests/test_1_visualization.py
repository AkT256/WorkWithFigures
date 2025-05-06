# tests/test_1_visualization.py
"""
Тест 1. Визуализация (пункт 1)
"""

import sys
import os

# Добавляет в sys.path корень проекта (папку на уровень выше tests/)
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from itertools import islice
import matplotlib.pyplot as plt

from polygons_api.generators import gen_rectangle
from polygons_api.visualization import visualize_polygons


def demo():
    # П.1.1:
    it = gen_rectangle(width=1, height=1, dx=2)
    first = next(it)
    print("П.1.1: первый прямоугольник:", first)

    # П.1.2:
    seq = [first] + list(islice(it, 4))
    print("П.1.2: все 5 прямоугольников:", seq)

    # П.1.3:
    buf = visualize_polygons(iter(seq), limit=5)
    img = plt.imread(buf)
    plt.imshow(img)
    plt.axis('off')
    plt.title("5 прямоугольников")
    plt.show()


if __name__ == "__main__":
    demo()