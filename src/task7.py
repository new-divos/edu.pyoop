#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def is_adult(self) -> bool:
        return self.age >= 18
