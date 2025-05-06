# tests/test_7_decorators.py
"""
Тест 7. Декораторы (пункт 7)

7.1 Фильтрующие декораторы: демонстрируем работу фильтра flt_short_side
    на наборе разных, разнесённых по Y фигур (прямоугольники, треугольники, шестиугольники),
    оставляя только те, у которых есть очень короткая сторона.
7.2 Преобразующие декораторы: демонстрируем работу tr_rotate
    на равносторонних треугольниках (поворачиваем их на 45°).

Результат выводится в одном окне: 2×2 подграфика, «до»/«после» для каждого случая.
"""

import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from itertools import islice

from polygons_api.generators import gen_rectangle, gen_triangle, gen_hexagon
from polygons_api.decorators import decorator_filter, decorator_transform
from polygons_api.filters    import flt_short_side
from polygons_api.transforms import tr_rotate, tr_translate


# --- 7.1 Декоратор-фильтр по короткой стороне (< threshold) ---
@decorator_filter(flt_short_side(1.1))
def only_short(seq):
    """
    П.7.1: оставляет только те фигуры, у которых есть сторона короче 1.1.
    """
    return list(seq)


# --- 7.2 Декоратор-поворот на 45° ---
@decorator_transform(tr_rotate(45))
def rotated_polygons(seq):
    """
    П.7.2: поворачивает каждый полигон на 45°.
    """
    return list(seq)


def demo():
    # подготовка базовых фигур, разнесённых по Y, чтобы не пересекались
    rects = list(islice(gen_rectangle(width=2, height=1, dx=3), 4))
    tris  = [tr_translate(0, 3)(p) for p in islice(gen_triangle(size=2, dx=3), 4)]
    hexs  = [tr_translate(0, 6)(p) for p in islice(gen_hexagon(size=1.5, dx=3), 4)]
    shapes1 = rects + tris + hexs

    filtered1 = only_short(iter(shapes1))
    
    # 7.2: первые 7 треугольников для показа поворота
    base_tris = list(islice(gen_triangle(size=1.5, dx=2), 7))
    rotated  = rotated_polygons(iter(base_tris))

    fig, axes = plt.subplots(2, 2, figsize=(12, 10), sharex=True, sharey=True)
    (ax1_before, ax1_after), (ax2_before, ax2_after) = axes

    # --- П.7.1: фильтрация ---
    ax1_before.set_title("7.1 До фильтрации (12 фигур)")
    for poly in shapes1:
        xs, ys = zip(*poly)
        ax1_before.plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    ax1_before.axis('off')
    ax1_before.set_aspect('equal', adjustable='box')

    ax1_after.set_title(f"7.1 После ({len(filtered1)} фигур)")
    for poly in filtered1:
        xs, ys = zip(*poly)
        ax1_after.plot(xs + (xs[0],), ys + (ys[0],), color='green')
    ax1_after.axis('off')
    ax1_after.set_aspect('equal', adjustable='box')

    # --- П.7.2: преобразование ---
    ax2_before.set_title("7.2 До поворота (7 треугольников)")
    for poly in base_tris:
        xs, ys = zip(*poly)
        ax2_before.plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    ax2_before.axis('off')
    ax2_before.set_aspect('equal', adjustable='box')

    ax2_after.set_title("7.2 После поворота на 45°")
    for poly in rotated:
        xs, ys = zip(*poly)
        ax2_after.plot(xs + (xs[0],), ys + (ys[0],), color='blue')
    ax2_after.axis('off')
    ax2_after.set_aspect('equal', adjustable='box')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()