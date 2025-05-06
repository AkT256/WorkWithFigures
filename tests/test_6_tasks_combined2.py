# tests/test_6_tasks_combined.py
"""
Тест 6. Комбинированные задачи (пункт 6)
"""

import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from math import cos, sin, pi
from shapely.geometry import Polygon as ShapelyPolygon
from itertools import islice

from polygons_api.transforms   import tr_translate, tr_homothety, tr_rotate
from polygons_api.filters      import flt_square, flt_short_side
from polygons_api.generators   import gen_rectangle, gen_triangle


def demo():
    fig, axes = plt.subplots(3, 2, figsize=(12, 15))

       # П.6.1 — фильтрация фигур, созданных в п. 4.4 (оставляем 6)
    base_trap = [(0, 0), (1, 0), (0.9, 0.2), (0.1, 0.2)]
    cx = sum(x for x, _ in base_trap) / len(base_trap)
    cy = sum(y for _, y in base_trap) / len(base_trap)
    centered = [(x - cx, y - cy) for x, y in base_trap]

    scales = range(1, 5) 
    step = 0.4
    scale_factor = 0.2

    shapes1 = []
    for k in scales:
        s = 1 + scale_factor * k 
        trap = tr_homothety(s)(centered)
        trap_r  = tr_rotate(135)(trap)
        trap_rt = tr_translate( k*step,  k*step)(trap_r)
        shapes1.append(trap_rt)
        trap_r2  = tr_rotate(-45)(trap)
        trap_rt2 = tr_translate(-k*step, -k*step)(trap_r2)
        shapes1.append(trap_rt2)

    threshold = 0.55
    filtered1 = list(filter(flt_square(threshold), shapes1))

    ax_before, ax_after = axes[0,0], axes[0,1]
    ax_before.set_title(f"6.1 До (8 трапеций)")
    for poly in shapes1:
        xs, ys = zip(*poly)
        ax_before.plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    ax_before.axis('equal'); ax_before.axis('off')

    ax_after.set_title(f"6.1 После ({len(filtered1)} трапеций)")
    for poly in filtered1:
        xs, ys = zip(*poly)
        ax_after.plot(xs + (xs[0],), ys + (ys[0],), color='blue')
    ax_after.axis('equal'); ax_after.axis('off')


    # П.6.2 — 7 разных фигур, фильтр по короткой стороне <0.8
    shapes2 = [
        tr_translate(0, 0)([(0, 0), (1, 0), (1, 0.3), (0, 0.3)]),
        tr_translate(3, 0)([(0, 0), (0.5, 1), (1, 0)]),
        tr_translate(6, 0)([(cos(a), sin(a)) for a in [pi/3 * j for j in range(6)]]),
        tr_translate(0, 2)([(0, 0), (1.2, 0), (1, 0.2), (0.2, 0.2)]),
        tr_translate(3, 2)([(0, 0), (1, 0), (1, 1), (0, 1)]),
        tr_translate(6, 2)([(0, 0), (0.7, 1.4), (1.4, 0)]),
        tr_translate(0, 4)([(0, 0), (2, 0), (2, 0.5), (0, 0.5)])
    ]
    filtered2 = list(filter(flt_short_side(0.8), shapes2))

    axes[1, 0].set_title("6.2 До фильтрации (7 фигур)")
    for poly in shapes2:
        xs, ys = zip(*poly)
        axes[1, 0].plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    axes[1, 0].axis("equal"); axes[1, 0].axis("off")

    axes[1, 1].set_title(f"6.2 После фильтрации ({len(filtered2)} фигур)")
    for poly in filtered2:
        xs, ys = zip(*poly)
        axes[1, 1].plot(xs + (xs[0],), ys + (ys[0],), color='blue')
    axes[1, 1].axis("equal"); axes[1, 1].axis("off")

    # П.6.3
    base = [(0, 0), (2, 0), (2, 1), (0, 1)]

    # Генерирует 15 «перекрывающихся» прямоугольников
    shapes3 = [
        tr_translate(k * 0.5, 0)(
            tr_homothety(1 + 0.1 * k)(base)
        )
        for k in range(15)
    ]

    threshold = 5.8
    filtered3 = list(filter(flt_square(threshold), shapes3))


    ax_before, ax_after = axes[2, 0], axes[2, 1]

    ax_before.set_title("6.3 До фильтрации (15 фигур)")
    for poly in shapes3:
        xs, ys = zip(*poly)
        ax_before.plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    ax_before.axis("equal"); ax_before.axis("off")

    ax_after.set_title(f"6.3 После фильтрации ({len(filtered3)} фигур)")
    for poly in filtered3:
        xs, ys = zip(*poly)
        ax_after.plot(xs + (xs[0],), ys + (ys[0],), color='blue')
    ax_after.axis("equal"); ax_after.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()
