#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from task4 import Point


def test_point1(capsys: pytest.CaptureFixture) -> None:
    p1 = Point()

    p1.set_coordinates(6, 8)
    p1.display()
    capture = capsys.readouterr()
    assert capture.out == "Point(6, 8)\n"

    assert p1.get_distance_to_origin() == 10.0


def test_point2(capsys: pytest.CaptureFixture) -> None:
    p2 = Point()
    p2.display()
    capture = capsys.readouterr()
    assert capture.out == "Координаты не заданы\n"

    p2.set_coordinates(3, 4)
    p2.display()
    capture = capsys.readouterr()
    assert capture.out == "Point(3, 4)\n"

    p2.get_distance_to_origin() == 5.0


def test_point3(capsys: pytest.CaptureFixture) -> None:
    p3 = Point()
    p3.display()
    capture = capsys.readouterr()
    assert capture.out == "Координаты не заданы\n"

    assert p3.get_distance_to_origin() is None

    p3.x = 4
    p3.display()
    capture = capsys.readouterr()
    assert capture.out == "Координаты не заданы\n"

    assert p3.get_distance_to_origin() is None

    p3.y = 3
    p3.display()
    capture = capsys.readouterr()
    assert capture.out == "Point(4, 3)\n"

    assert p3.get_distance_to_origin() == 5.0
