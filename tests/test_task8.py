#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task8 import Dog


def test_curt() -> None:
    curt = Dog("Curt", 4)
    assert isinstance(curt, Dog)
    assert curt.name == "Curt"
    assert curt.age == 4
    assert curt.description() == "Curt is 4 years old"
    assert curt.speak("Wo") == "Curt says Wo"
    assert curt.speak("Bow") == "Curt says Bow"


def test_jack() -> None:
    jack = Dog("Jack", 12)
    assert isinstance(jack, Dog)
    assert jack.name == "Jack"
    assert jack.age == 12
    assert jack.description() == "Jack is 12 years old"
    assert jack.speak("Woof Woof") == "Jack says Woof Woof"
    assert jack.speak("Bow Wow") == "Jack says Bow Wow"


def test_karl() -> None:
    assert Dog("Karl", 6).description() == "Karl is 6 years old"
