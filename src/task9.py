#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing
from numbers import Number


class Mesuarable(typing.Protocol):
    def __add__(self: "NumericType", other: "NumericType") -> "NumericType": ...

    def __mul__(
        self: "NumericType", other: typing.Union["NumericType", Number]
    ) -> "NumericType": ...


NumericType = typing.TypeVar("NumericType", bound=Mesuarable)


class Rectangle(typing.Generic[NumericType]):
    def __init__(self, width: NumericType, height: NumericType) -> None:
        self.width = width
        self.height = height

    def area(self) -> NumericType:
        return self.width * self.height

    def perimeter(self) -> NumericType:
        return (self.width + self.height) * typing.cast(Number, 2)
