# tests/test_4_examples.py
"""
Тест 4. Примеры (пункт 4)
"""

import sys
import os
import matplotlib.pyplot as plt
from itertools import islice
from math import sin, cos, radians

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from polygons_api.generators import gen_rectangle, gen_triangle
from polygons_api.transforms   import tr_translate, tr_rotate, tr_symmetry, tr_homothety


def demo():
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.flatten()

    # П.4.1
    angle = 30
    θ = radians(angle)
    nx, ny = -sin(θ), cos(θ)
    offsets = [0, 1.5, 3]
    for off in offsets:
        seq = islice(
            map(lambda p: tr_translate(nx*off, ny*off)(tr_rotate(angle)(p)),
                gen_rectangle(dx=2)),
            7
        )
        for poly in seq:
            xs, ys = zip(*poly)
            axes[0].plot(xs + (xs[0],), ys + (ys[0],), color='blue')
    axes[0].set_title("4.1 Three parallel rectangle lanes (30°)")
    axes[0].set_aspect('equal')
    axes[0].axis('off')

    # П.4.2
    N = 7
    dx = 2
    center_offset = dx * (N - 1) / 2
    angle = 45
    seq_b1 = islice(
        map(lambda p: tr_rotate(angle)(tr_translate(-center_offset, 0)(p)),
            gen_rectangle(dx=dx)),
        N
    )
    seq_b2 = islice(
        map(lambda p: tr_rotate(-angle)(tr_translate(-center_offset, 0)(p)),
            gen_rectangle(dx=dx)),
        N
    )
    for poly in list(seq_b1) + list(seq_b2):
        xs, ys = zip(*poly)
        axes[1].plot(xs + (xs[0],), ys + (ys[0],), color='green')
    axes[1].set_title("4.2 Two crossing rectangle lanes (45° centered)")
    axes[1].set_aspect('equal')
    axes[1].axis('off')

    # П.4.3
    seq_c1 = islice(map(lambda p: tr_translate(0, -1)(p), gen_triangle(dx=2)), 7)
    seq_c2 = islice(map(lambda p: tr_translate(0, 1)(tr_symmetry('x')(p)), gen_triangle(dx=2)), 7)
    for poly in list(seq_c1) + list(seq_c2):
        xs, ys = zip(*poly)
        axes[2].plot(xs + (xs[0],), ys + (ys[0],), color='red')
    axes[2].set_title("4.3 Two triangle lanes symmetric across X-axis")
    axes[2].set_aspect('equal')
    axes[2].axis('off')

    # П.4.4
    base_trap = [(0, 0), (1, 0), (0.9, 0.2), (0.1, 0.2)]
    cx = sum(x for x, _ in base_trap) / len(base_trap)
    cy = sum(y for _, y in base_trap) / len(base_trap)
    centered = [(x - cx, y - cy) for x, y in base_trap]

    scales = range(1, 5)
    step = 0.4
    scale_factor = 0.2

    for k in scales:
        trap = tr_homothety(1 + scale_factor * k)(centered)
        trap_r = tr_rotate(135)(trap)
        trap_rt = tr_translate(k * step, k * step)(trap_r)
        xs, ys = zip(*trap_rt)
        axes[3].plot(xs + (xs[0],), ys + (ys[0],), color='purple')

    for k in scales:
        trap = tr_homothety(1 + scale_factor * k)(centered)
        trap_r = tr_rotate(-45)(trap)
        trap_rt = tr_translate(-k * step, -k * step)(trap_r)
        xs, ys = zip(*trap_rt)
        axes[3].plot(xs + (xs[0],), ys + (ys[0],), color='orange')

    axes[3].set_title("4.4 Two cones of trapezoids in I and III")
    axes[3].set_aspect('equal')
    axes[3].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    demo()
