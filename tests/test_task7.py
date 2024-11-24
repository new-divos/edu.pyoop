#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task7 import Person


def test_ash() -> None:
    p1 = Person("Ash", "Ketchum", 20)
    assert isinstance(p1, Person)
    assert p1.full_name() == "Ketchum Ash"
    assert p1.age == 20
    assert p1.first_name == "Ash"
    assert p1.last_name == "Ketchum"
    assert p1.is_adult() is True


def test_hermione() -> None:
    p2 = Person("Hermione", "Granger", 16)
    assert isinstance(p2, Person)
    assert p2.age == 16
    assert p2.first_name == "Hermione"
    assert p2.last_name == "Granger"
    assert p2.full_name() == "Granger Hermione"
    assert p2.is_adult() is False
