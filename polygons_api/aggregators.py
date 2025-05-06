"""
aggregators.py — Модуль 8: агрегирующие функции для списков полигонов
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from functools import reduce
from shapely.geometry import Polygon as ShapelyPolygon
from typing import List, Tuple
from polygons_api.models import Point, Polygon, PolygonSeq

def agr_origin_nearest(seq: PolygonSeq) -> Point:
    """
    8.1 Находит точку среди всех полигонов, ближайшую к (0,0).

    Параметры:
        seq (PolygonSeq): итератор полигонов.

    Возвращает:
        Point: координаты ближайшей точки.
    """
    best_pt, best_d = None, float('inf')
    for poly in seq:
        for x, y in poly:
            d = x*x + y*y
            if d < best_d:
                best_d, best_pt = d, (x, y)
    return best_pt

def agr_max_side(seq: PolygonSeq) -> float:
    """
    8.2 Вычисляет длину самой длинной стороны среди всех полигонов.

    Параметры:
        seq (PolygonSeq): итератор полигонов.

    Возвращает:
        float: максимальная длина стороны.
    """
    max_len = 0.0
    for poly in seq:
        pts = list(poly) + [poly[0]]
        for (x1,y1), (x2,y2) in zip(pts, pts[1:]):
            length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            if length > max_len:
                max_len = length
    return max_len

def agr_min_area(seq: List[Polygon]) -> Polygon:
    """
    8.3 Находит многоугольник с минимальной площадью.

    Параметры:
        seq (List[Polygon]): список полигонов.

    Возвращает:
        Polygon: полигон с минимальной площадью.
    """
    return min(seq, key=lambda p: ShapelyPolygon(p).area)

def agr_perimeter(seq: PolygonSeq) -> float:
    """
    8.4 Считает общий периметр всех полигонов.

    Параметры:
        seq (PolygonSeq): итератор полигонов.

    Возвращает:
        float: суммарная длина всех сторон.
    """
    return reduce(lambda acc, poly: acc + ShapelyPolygon(poly).length,
                  seq, 0.0)

def agr_area(seq: PolygonSeq) -> float:
    """
    8.5 Считает общую площадь всех полигонов.

    Параметры:
        seq (PolygonSeq): итератор полигонов.

    Возвращает:
        float: суммарная площадь.
    """
    return reduce(lambda acc, poly: acc + ShapelyPolygon(poly).area,
                  seq, 0.0)