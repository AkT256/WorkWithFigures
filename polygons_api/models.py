"""
models.py — Модели и типы данных для работы с полигонами
"""

from typing import Tuple, Iterator

# Одна точка в 2D
Point = Tuple[float, float]
# Многоугольник — кортеж точек
Polygon = Tuple[Point, ...]
# Последовательность многоугольников (итератор)
PolygonSeq = Iterator[Polygon]