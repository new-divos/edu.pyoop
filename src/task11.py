#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any


class Stack:
    def __init__(self):
        self.values = []

    def push(self, item: Any) -> None:
        self.values.append(item)

    def pop(self) -> Any | None:
        if len(self.values) == 0:
            print("Empty Stack")
            return None
        else:
            return self.values.pop()

    def peek(self) -> Any | None:
        if len(self.values) == 0:
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self) -> bool:
        return len(self.values) == 0

    def size(self) -> int:
        return len(self.values)
