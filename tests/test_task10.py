#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task10 import Numbers


def test_numbers1() -> None:
    nums = Numbers(1, 2, -4, -5, 3)

    assert nums.get_positive() == [1, 2, 3]
    assert nums.get_negative() == [-4, -5]
    assert nums.get_zeroes() == []


def test_numbers2() -> None:
    nums = Numbers(10, 20, 30, 0, 0, 5)

    assert nums.get_positive() == [10, 20, 30, 5]
    assert nums.get_zeroes() == [0, 0]

    nums.add_number(100)
    nums.add_number(0)
    nums.add_number(7)

    assert nums.get_positive() == [10, 20, 30, 5, 100, 7]
    assert nums.get_zeroes() == [0, 0, 0]


def test_numbers3() -> None:
    nums = Numbers(7, 8, 9)
    nums_2 = Numbers(7, 8, 9)

    nums.add_number(10)
    nums_2.add_number(11)
    nums_2.add_number(12)

    assert nums.get_positive() == [7, 8, 9, 10]
    assert nums_2.get_positive() == [7, 8, 9, 11, 12]


def test_numbers4() -> None:
    nums = Numbers(-1, -2, -3, 0, -6, -4, 0, 0)

    assert nums.get_positive() == []
    assert nums.get_negative() == [-1, -2, -3, -6, -4]
    assert nums.get_zeroes() == [0, 0, 0]


def test_numbers5() -> None:
    nums = Numbers()
    assert nums.get_positive() == []
    assert nums.get_negative() == []
    assert nums.get_zeroes() == []

    nums.add_number(5)
    nums.add_number(3)
    nums.add_number(4)

    assert nums.get_positive() == [5, 3, 4]
    assert nums.get_negative() == []
    assert nums.get_zeroes() == []
