#!/usr/bin/env python
from __future__ import annotations
from random import randint


class Uwp:
    def __init__(self: Uwp) -> Uwp:
        [self.s, self.p] = [base(), base()]

        self.a = max(0, self.s + flux())
        self.h = min(10, max(0, self.a + flux()))

        self.g = max(0, self.p + flux())
        self.l = max(0, self.g + flux())

    def __str__(self: Uwp) -> str:
        return (
            f"{ehex(self.s)}{ehex(self.a)}{ehex(self.h)}"
            f"{ehex(self.p)}{ehex(self.g)}{ehex(self.l)}"
            f"-{ehex(d(6))}"
        )


def d(x: int) -> int:
    return randint(1, x)


def flux() -> int:
    return d(6) - d(6)


def base() -> int:
    return d(6) + d(6) - 2


def ehex(num: int) -> str:
    assert(num >= 0)

    if num < 10:
        return str(num)
    else:
        return chr(45 + num)
