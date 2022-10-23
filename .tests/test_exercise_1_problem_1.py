#!/usr/bin/env python3


"""Test the submitted solutions for exercise 1, problem 1 of AutoGIS."""

import pytest

import shapely.geometry

from points_decorator import points
from import_notebook import import_notebook


exercise1 = import_notebook("Exercise-1-problem-1-2.ipynb")


class Test_Exercise_1_Problem_1:
    @points(1, "`create_point_geometry()` does not work as expected.")
    def test_create_point_geometry(self):
        point = exercise1.create_point_geometry(0.0, 1.1)
        assert point == shapely.geometry.Point(0.0, 1.1)

    @points(1, "Take another look at `create_line_geometry()`!")
    def test_create_line_geometry(self):
        points = [
            shapely.geometry.Point(1, 2),
            shapely.geometry.Point(3, 4)
        ]
        line = exercise1.create_line_geometry(points)
        assert line == shapely.geometry.LineString(points)

    @points(
        0.5,
        "Does your function `create_line_geometry()` "
        "check that its input is a list?"
    )
    def test_create_line_geometry_input_is_list(self):
        with pytest.raises(AssertionError):
            _ = exercise1.create_line_geometry("NOT A LIST")

    @points(
        0.5,
        "Does your function `create_line_geometry()` "
        "check that its input has at least two points?"
    )
    def test_create_line_geometry_min_two_values(self):
        with pytest.raises(AssertionError):
            # only one point
            _ = exercise1.create_line_geometry([shapely.geometry.Point(1, 2)])

    @points(bonus_task=True)
    def test_create_line_geometry_test_if_all_points(self):
        with pytest.raises(AssertionError):
            # not shapely.geometry.Point
            _ = exercise1.create_line_geometry([(1, 2), (3, 4)])

    @points(
        1,
        "The function `create_polygon_geometry()` still has some hick-ups."
    )
    def test_create_polygon_geometry(self):
        polygon = exercise1.create_polygon_geometry(
            [(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)]
        )
        assert polygon == shapely.geometry.Polygon(
            [(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)]
        )

    @points(
        0.33,
        "Does your function `create_polygon_geometry()` "
        "check that its input is a list?"
    )
    def test_create_polygon_geometry_input_is_list(self):
        with pytest.raises(AssertionError):
            _ = exercise1.create_polygon_geometry("NOT A LIST")

    @points(
        0.33,
        "Does your function `create_polygon_geometry()` "
        "check that its input has at least three tuples?"
    )
    def test_create_polygon_geometry_min_three_values(self):
        with pytest.raises(AssertionError):
            # only one tuple
            _ = exercise1.create_polygon_geometry([(1, 2)])
        with pytest.raises(AssertionError):
            # only two tuples
            _ = exercise1.create_polygon_geometry([(1, 2), (3, 4)])

    @points(
        0.34,
        "The function `create_polygon_geometry()` does not check "
        "whether all input values are tuples of two values."
    )
    def test_create_polygon_geometry_check_two_valued_tuples(self):
        with pytest.raises(AssertionError):
            _ = exercise1.create_polygon_geometry([(1,), (2, 3), (4, 5)])
        with pytest.raises(AssertionError):
            _ = exercise1.create_polygon_geometry([(1, 2), (3), (4, 5)])

    @points(bonus_task=True)
    def test_create_polygon_geometry_check_tuple_values_float_or_int(self):
        with pytest.raises(AssertionError):
            _ = exercise1.create_polygon_geometry(
                [("a", "b"), ("c", "d"), ("e", "f")]
            )

    @points(bonus_task=True)
    def test_create_polygon_geometry_accept_tuples_or_points(self):
        polygon_a = exercise1.create_polygon_geometry(
            [(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)]
        )
        polygon_b = exercise1.create_polygon_geometry(
            [
                shapely.geometry.Point(45.2, 22.34),
                shapely.geometry.Point(100.22, -3.20),
                shapely.geometry.Point(70.0, 10.20)
            ]
        )
        assert polygon_a == polygon_b == shapely.geometry.Polygon(
            [(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)]
        )
