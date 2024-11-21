#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from task5 import SoccerPlayer


def test_leo(capsys: pytest.CaptureFixture) -> None:
    leo = SoccerPlayer("Leo", "Messi")
    assert isinstance(leo, SoccerPlayer)
    assert leo.__dict__ == {"name": "Leo", "surname": "Messi", "goals": 0, "assists": 0}
    leo.score(700)
    assert leo.goals == 700
    leo.make_assist(500)
    assert leo.assists == 500

    leo.statistics()
    capture = capsys.readouterr()
    assert capture.out == "Messi Leo - голы: 700, передачи: 500\n"


def test_kokorin(capsys: pytest.CaptureFixture) -> None:
    kokorin = SoccerPlayer("Alex", "Kokorin")
    assert isinstance(kokorin, SoccerPlayer)
    assert kokorin.name == "Alex"
    assert kokorin.surname == "Kokorin"
    assert kokorin.assists == 0
    assert kokorin.goals == 0
    kokorin.score()
    assert kokorin.goals == 1
    kokorin.score(5)
    assert kokorin.goals == 6
    kokorin.make_assist()
    assert kokorin.assists == 1
    kokorin.make_assist(10)
    assert kokorin.assists == 11

    kokorin.statistics()
    capture = capsys.readouterr()
    assert capture.out == "Kokorin Alex - голы: 6, передачи: 11\n"


def test_obi(capsys: pytest.CaptureFixture) -> None:
    obi = SoccerPlayer("Оби-Ван", "Кеноби")
    obi.make_assist()
    assert obi.name == "Оби-Ван"
    assert obi.surname == "Кеноби"
    assert obi.__dict__ == {
        "name": "Оби-Ван",
        "surname": "Кеноби",
        "goals": 0,
        "assists": 1,
    }

    obi.statistics()
    capture = capsys.readouterr()
    assert capture.out == "Кеноби Оби-Ван - голы: 0, передачи: 1\n"


def test_mila(capsys: pytest.CaptureFixture) -> None:
    mila = SoccerPlayer("Mila", "Kunis")
    mila.make_assist()

    mila.statistics()
    capture = capsys.readouterr()
    assert capture.out == "Kunis Mila - голы: 0, передачи: 1\n"
