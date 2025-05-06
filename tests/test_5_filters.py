# tests/test_5_filters.py
"""
Тест 5. Фильтры (пункт 5)
"""

import sys
import os

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math import sin, cos, pi
from polygons_api.filters import (
    flt_convex_polygon,
    flt_angle_point,
    flt_square,
    flt_short_side,
    flt_point_inside,
    flt_polygon_angles_inside,
)

def demo():
    # П.5.0: создаёт разные многоугольники
    shapes = [
        [(0, 0), (1, 0), (1, 0.4), (0, 0.4)],  # маленький прямоугольник
        [(3, 1), (6, 1), (6, 4), (3, 4)],      # большой прямоугольник
        [(0, 0), (0.5, 1), (1, 0)],            # равносторонний треугольник
        [(4, 2), (5, 4), (6, 2)],              # смещённый треугольник
        # правильный шестиугольник радиуса 0.5
        [(0.5 * cos(a), 0.5 * sin(a)) for a in [pi/3 * j for j in range(6)]],
        # шестиугольник радиуса 1, смещённый на (3,2)
        [(3 + cos(a), 2 + sin(a)) for a in [pi/3 * j for j in range(6)]],
        # не выпуклый многоугольник
        [(1, 1), (2, 1), (1.5, 1.5), (2, 2), (1, 3), (0, 2), (1, 1)]
    ]
    total = len(shapes)
    print("Всего фигур:", total)

    # П.5.1–П.5.6: применяет фильтры
    filters = {
        "5.1 Convex": flt_convex_polygon,
        "5.2 Angle at (0,0)": flt_angle_point((0, 0)),
        "5.3 Area < 3.0": flt_square(3.0),
        "5.4 Short side < 0.9": flt_short_side(0.9),
        "5.5 Contains (0.5,0.5)": flt_point_inside((0.5, 0.5)),
        "5.6 Contains rect2 angles": flt_polygon_angles_inside([
            (3, 1), (6, 1), (6, 4), (3, 4)
        ])
    }

    for label, func in filters.items():
        filtered = list(filter(func, shapes))
        count = len(filtered)
        print(f"{label}: {count}/{total}")

if __name__ == "__main__":
    demo()
