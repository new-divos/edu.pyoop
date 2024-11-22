#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Zebra:
    def __init__(self):
        self.is_white = True

    def which_stripe(self) -> None:
        if self.is_white:
            print("Полоска белая")
        else:
            print("Полоска черная")

        self.is_white = not self.is_white

    def run_away(self) -> None:
        print("Oh, Sugar Honey Ice Tea")
