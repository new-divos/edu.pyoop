#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from task3 import Point


def test_points(capsys: pytest.CaptureFixture) -> None:
    p1 = Point()
    p2 = Point()
    assert isinstance(p1, Point)
    assert isinstance(p2, Point)

    p1.set_coordinates(1, 2)
    assert p1.x == 1
    assert p1.y == 2
    p2.set_coordinates(4, 6)
    assert p2.x == 4
    assert p2.y == 6
    assert p1.get_distance(p2) == 5.0
    p3 = Point()
    p3.set_coordinates(10, 10)
    p1.set_coordinates(4, 2)
    assert p1.get_distance(p3) == 10.0

    # Распечатает "Передана не точка", вернет None
    res = p1.get_distance(10)
    # Метод get_distance должен возвращать None, если в него
    # была передана не точка
    assert res is None
    captured = capsys.readouterr()
    assert captured.out == "Передана не точка\n"

    # Распечатает "Передана не точка", вернет None
    assert p2.get_distance([1, 2, 3]) is None
    captured = capsys.readouterr()
    assert captured.out == "Передана не точка\n"
