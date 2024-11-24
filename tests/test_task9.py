#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task9 import Rectangle


def test_rectangle1() -> None:
    r1 = Rectangle(2, 3)
    assert r1.width == 2
    assert r1.height == 3
    assert r1.perimeter() == 10
    assert r1.area() == 6


def test_rectangle2() -> None:
    r2 = Rectangle(10, 0.5)
    assert r2.width == 10
    assert r2.height == 0.5
    assert r2.perimeter() == 21.0
    assert r2.area() == 5.0
