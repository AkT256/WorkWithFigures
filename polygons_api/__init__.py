"""
polygons — пакет для генерации, трансформации и фильтрации многоугольников
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from polygons_api.models import Point, Polygon, PolygonSeq
from polygons_api.generators import gen_rectangle, gen_triangle, gen_hexagon
from polygons_api.transforms import tr_translate, tr_rotate, tr_symmetry, tr_homothety
from polygons_api.filters import (
    flt_convex_polygon, flt_angle_point, flt_square,
    flt_short_side, flt_point_inside, flt_polygon_angles_inside
)
from polygons_api.combinators import zip_polygons, count_2D, zip_tuple
from polygons_api.aggregators import (
    agr_origin_nearest, agr_max_side, agr_min_area,
    agr_perimeter, agr_area
)
from polygons_api.decorators import decorator_filter, decorator_transform
from polygons_api.visualization import visualize_polygons