# tests/test_9_combinators.py
"""
Тест 9. Комбинаторы (пункт 9)

9.1 zip_polygons — поэлементное объединение нескольких потоков полигонов  
9.2 count_2D     — генерация 2D-счётчика; визуализируем точки и подписываем  
9.3 zip_tuple    — комбинирование точек из нескольких итераторов; визуализируем соединяющими отрезками  
"""

import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from itertools import islice, count, zip_longest

from polygons_api.combinators import zip_polygons, count_2D, zip_tuple
from polygons_api.generators  import gen_triangle
from polygons_api.transforms   import tr_symmetry


def demo():
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # 9.1 zip_polygons: ромбы из треугольников и их отражений
    N = 5
    tri_up   = list(islice(gen_triangle(size=1, dx=2), N))
    tri_down = [tr_symmetry('x')(p) for p in tri_up]
    rombs = list(zip_polygons(iter(tri_up), iter(tri_down)))

    axes[0].set_title("9.1 zip_polygons → ромбы")
    for poly in rombs:
        xs, ys = zip(*poly)
        axes[0].plot(xs + (xs[0],), ys + (ys[0],), lw=1.5)
    axes[0].axis('equal'); axes[0].axis('off')

    # 9.2 count_2D: точки по формуле
    pts = list(islice(count_2D(0, 10, step1=1, step2=2), 3))
    xs, ys = zip(*pts)

    axes[1].set_title("9.2 count_2D")
    axes[1].scatter(xs, ys, color='purple')
    for x, y in pts:
        axes[1].text(x, y, f"({x},{y})", fontsize=8, va='bottom')
    axes[1].grid(True); axes[1].axis('equal')

    # 9.3 zip_tuple: объединение точек из трёх списков
    seq1 = [(1,1), (2,2), (3,3), (4,4)]
    seq2 = [(2,2), (3,3), (4,4), (5,5)]
    seq3 = [(3,3), (4,4), (5,5), (6,6)]

    grouped = list(zip_tuple(iter(seq1), iter(seq2), iter(seq3)))

    axes[2].set_title("9.3 zip_tuple")
    for group in grouped:
        xs, ys = zip(*group)
        axes[2].plot(xs, ys, marker='o')
    axes[2].grid(True); axes[2].axis('equal')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()
