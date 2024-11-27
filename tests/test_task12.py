#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from task12 import Worker


def test_bob(capsys: pytest.CaptureFixture) -> None:
    bob = Worker("Bob Moore", 330000, "M", "1635777202")

    bob.get_info()
    capture = capsys.readouterr()
    assert capture.out == "Worker Bob Moore; passport-1635777202\n"
