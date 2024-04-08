#!/usr/bin/env python
from __future__ import annotations
from random import randint
from sys import stderr
from uwp import Uwp


class Subsector:
    X: int = 1
    Y: int = 1
    W: int = 8

    worlds = []

    def __str__(self) -> str:
        ret = ""
        for (pos, uwp) in self.worlds:
            ret += f"{pos} {uwp}\n"
        return ret

    def __init__(self) -> Subsector:
        x: int = self.X
        y: int = self.Y

        while y < self.Y + self.W:
            if randint(1, 6) < 4:
                self.worlds.append((f"{x:02d}{y:02d}", Uwp()))

            x += 1

            if x == self.W:
                y += 1
                x = self.X
