#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SoccerPlayer:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals: int = 1) -> None:
        self.goals += goals

    def make_assist(self, assists: int = 1) -> None:
        self.assists += assists

    def statistics(self) -> None:
        print(
            f"{self.surname} {self.name} - голы: {self.goals}, "
            f"передачи: {self.assists}"
        )
