#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from task2 import Counter


def test_counters(capsys: pytest.CaptureFixture) -> None:
    c1 = Counter()
    c2 = Counter()

    assert isinstance(c1, Counter)
    assert isinstance(c2, Counter)
    assert c1.__dict__ == {}
    assert c2.__dict__ == {}

    c1.start_from(45)
    assert len(c1.__dict__) == 1

    c1.increment()
    c1.display()  # печатает 46
    captured = capsys.readouterr()
    assert captured.out == "Текущее значение счетчика = 46\n"

    c1.increment()
    c1.display()  # печатает 47
    captured = capsys.readouterr()
    assert captured.out == "Текущее значение счетчика = 47\n"

    c2.start_from()
    c2.display()  # печатает 0
    captured = capsys.readouterr()
    assert captured.out == "Текущее значение счетчика = 0\n"

    c2.increment()
    c2.display()  # печатает 1
    captured = capsys.readouterr()
    assert captured.out == "Текущее значение счетчика = 1\n"

    c1.reset()  # обнулили с1, но с2 не должен меняться
    c1.display()  # печатает 0
    captured = capsys.readouterr()
    assert captured.out == "Текущее значение счетчика = 0\n"

    c2.display()  # попрежнему печатает 1
    captured = capsys.readouterr()
    assert captured.out == "Текущее значение счетчика = 1\n"
