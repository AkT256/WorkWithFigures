"""
transforms.py — Модуль 3: геометрические преобразования многоугольников
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from math import radians, cos, sin
from typing import Callable
from polygons_api.models import Point, Polygon

def tr_translate(dx: float = 0,
                 dy: float = 0) -> Callable[[Polygon], Polygon]:
    """
    3.1 Сдвигает все точки полигона на (dx, dy).

    Параметры:
        dx (float): смещение по X.
        dy (float): смещение по Y.

    Возвращает:
        Callable[[Polygon], Polygon]: функция, преобразующая полигон.
    """
    def _translate(poly: Polygon) -> Polygon:
        return tuple((x + dx, y + dy) for x, y in poly)
    return _translate

def tr_rotate(angle_deg: float = 0) -> Callable[[Polygon], Polygon]:
    """
    3.2 Поворачивает полигон на angle_deg градусов вокруг начала координат.

    Параметры:
        angle_deg (float): угол поворота в градусах.

    Возвращает:
        Callable[[Polygon], Polygon]: функция, применяющая поворот.
    """
    theta = radians(angle_deg)
    def _rotate(poly: Polygon) -> Polygon:
        return tuple((
            x * cos(theta) - y * sin(theta),
            x * sin(theta) + y * cos(theta)
        ) for x, y in poly)
    return _rotate

def tr_symmetry(axis: str = 'x') -> Callable[[Polygon], Polygon]:
    """
    3.3 Отражает полигон относительно оси X или Y.

    Параметры:
        axis (str): 'x' для отражения по X, любая другая строка — по Y.

    Возвращает:
        Callable[[Polygon], Polygon]: функция-отражатель.
    """
    if axis == 'x':
        def _sym(poly: Polygon) -> Polygon:
            return tuple((x, -y) for x, y in poly)
    else:
        def _sym(poly: Polygon) -> Polygon:
            return tuple((-x, y) for x, y in poly)
    return _sym

def tr_homothety(k: float = 1) -> Callable[[Polygon], Polygon]:
    """
    3.4 Масштабирует полигон относительно начала координат.

    Параметры:
        k (float): коэффициент масштабирования (>1 — увеличение, <1 — уменьшение).

    Возвращает:
        Callable[[Polygon], Polygon]: функция-масштабировщик.
    """
    def _scale(poly: Polygon) -> Polygon:
        return tuple((x * k, y * k) for x, y in poly)
    return _scale