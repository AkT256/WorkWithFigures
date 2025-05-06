"""
combinators.py — Модуль 9: «склейка» и «зип» последовательностей
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from typing import Iterator, Tuple
from itertools import zip_longest, count
from polygons_api.models import Point, Polygon, PolygonSeq

def zip_polygons(*iters: PolygonSeq) -> PolygonSeq:
    """
    9.1 Склеивает несколько итераторов многоугольников
    в один: конкатенирует вершины.

    Пример:
        zip_polygons(it1, it2) →
        [ poly1+poly2, poly3+poly4, … ]

    Возвращает:
        PolygonSeq: новый итератор.
    """
    return (sum(polys, ()) for polys in zip(*iters))

def count_2D(start1: int,
             start2: int,
             step1: int = 1,
             step2: int = 1) -> Iterator[Tuple[int,int]]:
    """
    9.2 Генерирует пары (i, j), инкрементируя каждую
    координату своим шагом.

    Параметры:
        start1 (int): начальное значение первой координаты.
        start2 (int): начальное значение второй координаты.
        step1 (int): шаг для первой координаты.
        step2 (int): шаг для второй координаты.

    Возвращает:
        Iterator[Tuple[int,int]]: пары (i, j).
    """
    return zip(count(start1, step1), count(start2, step2))

def zip_tuple(*iters: Iterator[Point]) -> Iterator[Tuple[Point,...]]:
    """
    9.3 Zip для кортежей точек: берёт по одной точке из каждого итератора.

    Возвращает:
        Iterator[Tuple[Point,...]]: итератор кортежей точек.
    """
    return zip(*iters)