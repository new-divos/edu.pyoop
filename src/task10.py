#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing


class Comparable(typing.Protocol):
    def __eq__(self: "NumericType", other: object) -> bool: ...

    def __ne__(self: "NumericType", other: object) -> bool: ...

    def __lt__(
        self: "NumericType", other: typing.Union["NumericType", int]
    ) -> bool: ...

    def __gt__(
        self: "NumericType", other: typing.Union["NumericType", int]
    ) -> bool: ...


NumericType = typing.TypeVar("NumericType", bound=Comparable)


class Numbers(typing.Generic[NumericType]):
    def __init__(self, *args: NumericType) -> None:
        self.numbers: list[NumericType] = [value for value in args]

    def add_number(self, value: NumericType) -> None:
        self.numbers.append(value)

    def get_positive(self) -> list[NumericType]:
        return [value for value in self.numbers if value > 0]

    def get_negative(self) -> list[NumericType]:
        return [value for value in self.numbers if value < 0]

    def get_zeroes(self) -> list[NumericType]:
        return [value for value in self.numbers if value == 0]
