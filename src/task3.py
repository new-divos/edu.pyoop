#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Point:
    def set_coordinates(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def get_distance(self, other: object) -> float | None:
        if isinstance(other, Point):
            return math.sqrt(
                (getattr(self, "x", 0.0) - getattr(other, "x", 0.0)) ** 2
                + (getattr(self, "y", 0.0) - getattr(other, "y", 0.0)) ** 2
            )
        else:
            print("Передана не точка")
            return None
