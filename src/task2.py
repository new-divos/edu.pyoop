#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Counter:
    def start_from(self, value: int = 0) -> None:
        self.current = value

    def increment(self) -> None:
        if hasattr(self, "current"):
            self.current += 1

    def display(self) -> None:
        if hasattr(self, "current"):
            print(f"Текущее значение счетчика = {self.current}")

    def reset(self) -> None:
        if hasattr(self, "current"):
            self.current = 0
