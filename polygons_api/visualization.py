"""
visualization.py — Модуль 1: функции для отрисовки последовательностей полигонов
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import matplotlib.pyplot as plt
from io import BytesIO
from polygons_api.models import PolygonSeq

def visualize_polygons(seq: PolygonSeq,
                       limit: int = 10) -> BytesIO:
    """
    1. Рисует первые limit полигонов из seq и возвращает
    изображение в виде байтового буфера PNG.

    Параметры:
        seq (PolygonSeq): итератор полигонов.
        limit (int): максимальное число отрисовываемых фигур.

    Возвращает:
        BytesIO: буфер с PNG-изображением.
    """
    fig, ax = plt.subplots()
    for i, poly in enumerate(seq):
        if i >= limit:
            break
        xs, ys = zip(*poly)
        ax.plot(list(xs) + [xs[0]], list(ys) + [ys[0]])
    ax.set_aspect('equal')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf