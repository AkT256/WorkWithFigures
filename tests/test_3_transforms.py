# tests/test_3_transforms.py
"""
Тест 3. Трансформации (пункт 3)
"""

import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from itertools import islice

from polygons_api.generators import gen_triangle
from polygons_api.transforms import (
    tr_translate,
    tr_rotate,
    tr_symmetry,
    tr_homothety
)


def demo():
    # П.3.1: берёт первые 5 равносторонних треугольников
    base_seq = list(islice(gen_triangle(size=1, dx=3), 5))

    # П.3.2: определяет операции преобразования
    ops = {
        "translate(2,5)": tr_translate(2, 5),
        "rotate(45)":     tr_rotate(45),
        "symmetry_x":     tr_symmetry('x'),
        "homothety(0.5)": tr_homothety(0.5),
    }

    # П.3.3: применяет каждую операцию к базовой последовательности
    results = {name: list(map(fn, base_seq)) for name, fn in ops.items()}

    # П.3.4: выводит в консоль для проверки
    print("Исходные треугольники:")
    for poly in base_seq:
        print(poly)
    for name, polys in results.items():
        print(f"\n{name}:")
        for poly in polys:
            print(poly)

    # П.3.5: вычисляет диапазоны осей для общей визуализации
    all_x = [x for polys in results.values() for poly in polys for x, _ in poly]
    all_y = [y for polys in results.values() for poly in polys for _, y in poly]
    xmin, xmax = min(all_x) - 0.5, max(all_x) + 0.5
    ymin, ymax = min(all_y) - 0.5, max(all_y) + 0.5

    # П.3.6: строит 4 подграфика с одинаковыми осями
    fig, axes = plt.subplots(1, len(ops), figsize=(4 * len(ops), 4), sharex=True, sharey=True)
    for ax, (name, polys) in zip(axes, results.items()):
        for poly in polys:
            xs, ys = zip(*poly)
            ax.plot(list(xs) + [xs[0]], list(ys) + [ys[0]])
        ax.set_title(name)
        ax.set_aspect('equal')
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        ax.grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()
