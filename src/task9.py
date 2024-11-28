#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    def area(self) -> int | float:
        return self.width * self.height

    def perimeter(self) -> int | float:
        return 2 * (self.width + self.height)
