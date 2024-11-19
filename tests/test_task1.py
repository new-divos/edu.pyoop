#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task1 import Config, create_instance


def test_config2() -> None:
    config_2 = create_instance(2)
    assert isinstance(config_2, Config)
    assert config_2.__dict__ == {"attribute1": "value1", "attribute2": "value2"}


def test_config4() -> None:
    config_4 = create_instance(4)
    assert isinstance(config_4, Config)
    assert config_4.__dict__ == {
        "attribute1": "value1",
        "attribute2": "value2",
        "attribute3": "value3",
        "attribute4": "value4",
    }


def test_config7() -> None:
    config_7 = create_instance(7)
    assert isinstance(config_7, Config)
    assert config_7.__dict__ == {
        "attribute1": "value1",
        "attribute2": "value2",
        "attribute3": "value3",
        "attribute4": "value4",
        "attribute5": "value5",
        "attribute6": "value6",
        "attribute7": "value7",
    }


def test_config10() -> None:
    config_10 = create_instance(10)
    assert isinstance(config_10, Config)
    assert config_10.__dict__ == {
        "attribute1": "value1",
        "attribute2": "value2",
        "attribute3": "value3",
        "attribute4": "value4",
        "attribute5": "value5",
        "attribute6": "value6",
        "attribute7": "value7",
        "attribute8": "value8",
        "attribute9": "value9",
        "attribute10": "value10",
    }
