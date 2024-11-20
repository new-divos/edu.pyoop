#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Point:
    def set_coordinates(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_distance_to_origin(self) -> float | None:
        if hasattr(self, "x") and hasattr(self, "y"):
            return math.sqrt(self.x**2 + self.y**2)

        return None

    def display(self) -> None:
        if hasattr(self, "x") and hasattr(self, "y"):
            print(f"Point({self.x}, {self.y})")
        else:
            print("Координаты не заданы")
