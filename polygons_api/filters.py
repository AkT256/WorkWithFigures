"""
filters.py — Модуль 5: операции фильтрации последовательностей многоугольников
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from typing import Callable
from shapely.geometry import Polygon as ShapelyPolygon
from polygons_api.models import Point, Polygon

def is_convex(polygon: Polygon) -> bool:
    """
    5.1 Проверяет, что многоугольник выпуклый.

    Параметры:
        polygon (Polygon): входной многоугольник.

    Возвращает:
        bool: True, если валидный, простой и совпадает с выпуклой оболочкой.
    """
    shp = ShapelyPolygon(polygon)
    return shp.is_valid and shp.is_simple and shp.convex_hull.equals(shp)

def flt_convex_polygon(polygon: Polygon) -> bool:
    """
    5.1 Фильтр выпуклых многоугольников.

    Параметры:
        polygon (Polygon): входной многоугольник.

    Возвращает:
        bool: True, если выпуклый.
    """
    return is_convex(polygon)

def flt_angle_point(point: Point) -> Callable[[Polygon], bool]:
    """
    5.2 Создаёт фильтр по наличию заданной точки в вершинах.

    Параметры:
        point (Point): искомая вершина.

    Возвращает:
        Callable[[Polygon], bool]: функция-фильтр.
    """
    def _has_angle(poly: Polygon) -> bool:
        return any(pt == point for pt in poly)
    return _has_angle

def flt_square(threshold: float) -> Callable[[Polygon], bool]:
    """
    5.3 Создаёт фильтр по площади < threshold.

    Параметры:
        threshold (float): максимальная допустимая площадь.

    Возвращает:
        Callable[[Polygon], bool]: функция-фильтр.
    """
    def _area_filter(poly: Polygon) -> bool:
        shp = ShapelyPolygon(poly)
        return shp.is_valid and shp.area < threshold
    return _area_filter

def flt_short_side(threshold: float) -> Callable[[Polygon], bool]:
    """
    5.4 Фильтр по кратчайшей стороне < threshold.

    Параметры:
        threshold (float): максимальная длина отсекаемых сторон.

    Возвращает:
        Callable[[Polygon], bool]: функция-фильтр.
    """
    def _has_short(poly: Polygon) -> bool:
        pts = list(poly) + [poly[0]]
        return any(
            ((x2 - x1)**2 + (y2 - y1)**2)**0.5 < threshold
            for (x1, y1), (x2, y2) in zip(pts, pts[1:])
        )
    return _has_short

def flt_point_inside(point: Point) -> Callable[[Polygon], bool]:
    """
    5.5 Создаёт фильтр, оставляющий многоугольники,
    содержащие точку point внутри.

    Параметры:
        point (Point): точка, которой проверяем наличие внутри.

    Возвращает:
        Callable[[Polygon], bool]: функция-фильтра.
    """
    def _inside(poly: Polygon) -> bool:
        shp = ShapelyPolygon(poly)
        return shp.is_valid and shp.contains(ShapelyPolygon([point]*3))
    return _inside

def flt_polygon_angles_inside(polygon: Polygon) -> Callable[[Polygon], bool]:
    """
    5.6 Создаёт фильтр, оставляющий многоугольники,
    содержащие хотя бы одну вершину заданного polygon.

    Параметры:
        polygon (Polygon): полигон, углы которого проверяем.

    Возвращает:
        Callable[[Polygon], bool]: функция-фильтр.
    """
    def _inside(poly2: Polygon) -> bool:
        shp2 = ShapelyPolygon(poly2)
        return shp2.is_valid and any(
            shp2.contains(ShapelyPolygon([pt]*3)) for pt in polygon
        )
    return _inside