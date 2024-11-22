#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from task6 import Zebra


def test_zebra1(capsys: pytest.CaptureFixture) -> None:
    zebra = Zebra()

    zebra.run_away()
    capture = capsys.readouterr()
    assert capture.out == "Oh, Sugar Honey Ice Tea\n"

    zebra.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"

    zebra.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска черная\n"

    zebra.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"

    zebra.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска черная\n"

    zebra.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"

    zebra.run_away()
    capture = capsys.readouterr()
    assert capture.out == "Oh, Sugar Honey Ice Tea\n"


def test_zebra2(capsys: pytest.CaptureFixture) -> None:
    zebra_1 = Zebra()
    zebra_2 = Zebra()

    zebra_1.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"

    zebra_2.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"

    zebra_1.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска черная\n"

    zebra_1.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"

    zebra_1.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска черная\n"

    zebra_2.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска черная\n"

    zebra_2.which_stripe()
    capture = capsys.readouterr()
    assert capture.out == "Полоска белая\n"
