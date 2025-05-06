"""
decorators.py — Модуль 7: декораторы для фильтров и трансформаций
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from functools import wraps
from typing import Callable, Iterator
from polygons_api.models import Polygon

def decorator_filter(filter_fn: Callable[[Polygon], bool]) -> Callable:
    """
    7.1 Декоратор, внедряющий фильтрацию в итератор-аргумент.

    Параметры:
        filter_fn (Callable[[Polygon], bool]): функция-фильтр.

    Возвращает:
        Callable: декоратор.
    """
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args2 = [filter(filter_fn, arg) if isinstance(arg, Iterator) else arg
                     for arg in args]
            return func(*args2, **kwargs)
        return wrapper
    return deco

def decorator_transform(transform_fn: Callable[[Polygon], Polygon]) -> Callable:
    """
    7.2 Декоратор, внедряющий преобразование (map) в итератор-аргумент.

    Параметры:
        transform_fn (Callable[[Polygon], Polygon]): функция-преобразователь.

    Возвращает:
        Callable: декоратор.
    """
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args2 = [map(transform_fn, arg) if isinstance(arg, Iterator) else arg
                     for arg in args]
            return func(*args2, **kwargs)
        return wrapper
    return deco