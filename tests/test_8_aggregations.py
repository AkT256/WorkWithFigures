# tests/test_8_aggregators.py
"""
Тест 8. Агрегаторы (пункт 8)

8.1 agr_origin_nearest — ближайшая к (0,0) вершина (визуализация + консоль)  
8.2 agr_max_side       — самая длинная сторона (визуализация + консоль)  
8.3 agr_min_area       — полигон с минимальной площадью (консоль)  
8.4 agr_perimeter      — суммарный периметр (консоль)  
8.5 agr_area           — суммарная площадь (консоль)  
"""

import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from itertools import islice

from polygons_api.generators  import gen_rectangle
from polygons_api.aggregators import (
    agr_origin_nearest,
    agr_max_side,
    agr_min_area,
    agr_perimeter,
    agr_area,
)


def demo():
    polys = list(islice(gen_rectangle(width=2, height=1, dx=2), 6))

    # П.8.1: ближайшая вершина к (0,0)
    nearest = agr_origin_nearest(iter(polys))
    print(f"8.1 Ближайшая вершина к (0,0): {nearest}")

    # П.8.2: длина самой длинной стороны
    max_len = agr_max_side(iter(polys))
    print(f"8.2 Длина самой длинной стороны: {max_len:.2f}")

    longest_seg = None
    for poly in polys:
        pts = list(poly) + [poly[0]]
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            if abs(length - max_len) < 1e-6:
                longest_seg = ((x1, y1), (x2, y2))
                break
        if longest_seg:
            break

    # П.8.3: полигон с минимальной площадью
    min_poly = agr_min_area(polys)
    print(f"8.3 Полигон с минимальной площадью: {min_poly}")

    # П.8.4: суммарный периметр
    total_perim = agr_perimeter(iter(polys))
    print(f"8.4 Суммарный периметр: {total_perim:.2f}")

    # П.8.5: суммарная площадь
    total_area = agr_area(iter(polys))
    print(f"8.5 Суммарная площадь: {total_area:.2f}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Визуализация 8.1
    ax1.set_title("8.1 Ближайшая вершина к (0,0)")
    for poly in polys:
        xs, ys = zip(*poly)
        ax1.plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    ax1.plot(*nearest, 'ro', markersize=8, label="Ближайшая")
    ax1.legend()
    ax1.set_aspect('equal'); ax1.grid(True)

    # Визуализация 8.2
    ax2.set_title("8.2 Самая длинная сторона")
    for poly in polys:
        xs, ys = zip(*poly)
        ax2.plot(xs + (xs[0],), ys + (ys[0],), color='gray')
    if longest_seg:
        (x1, y1), (x2, y2) = longest_seg
        ax2.plot([x1, x2], [y1, y2], color='red', lw=3, label="Макс. сторона")
    ax2.legend()
    ax2.set_aspect('equal'); ax2.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()
