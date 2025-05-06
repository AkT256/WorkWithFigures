"""
generators.py — Модуль 2: функции-генераторы последовательностей многоугольников
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from itertools import count
from math import cos, sin, pi
from polygons_api.models import Point, Polygon, PolygonSeq

def gen_rectangle(width: float = 1,
                  height: float = 1,
                  dx: float = 2) -> PolygonSeq:
    """
    2.1 Генерирует прямоугольники подряд вдоль оси X.

    Параметры:
        width (float): ширина прямоугольника.
        height (float): высота прямоугольника.
        dx (float): смещение по X между центрами соседних фигур.

    Возвращает:
        PolygonSeq: итератор, каждый элемент — кортеж из 4 точек-прямоугольника.
    """
    for i in count(0):
        x0 = i * dx
        yield (
            (x0,       0),         # левый-нижний
            (x0,       height),    # левый-верхний
            (x0+width, height),    # правый-верхний
            (x0+width, 0)          # правый-нижний
        )

def gen_triangle(size: float = 1,
                 dx: float = 2) -> PolygonSeq:
    """
    2.2 Генерирует равносторонние треугольники подряд вдоль оси X.

    Параметры:
        size (float): длина основания и высота треугольника.
        dx (float): смещение по X между фигурами.

    Возвращает:
        PolygonSeq: итератор кортежей из 3 точек-треугольников.
    """
    for i in count(0):
        x0 = i * dx
        yield (
            (x0,           0),      # левая вершина основания
            (x0 + size/2,  size),   # верхняя (середина)
            (x0 + size,    0)       # правая вершина основания
        )

def gen_hexagon(size: float = 1,
                dx: float = 2) -> PolygonSeq:
    """
    2.3 Генерирует правильные шестиугольники подряд вдоль оси X.

    Параметры:
        size (float): радиус описанной окружности.
        dx (float): смещение по X между центрами фигур.

    Возвращает:
        PolygonSeq: итератор кортежей точек-шестиугольников.
    """
    for i in count(0):
        x0 = i * dx
        yield tuple(
            (x0 + size * cos(angle), size * sin(angle))
            for angle in (pi/3 * j for j in range(6))
        )