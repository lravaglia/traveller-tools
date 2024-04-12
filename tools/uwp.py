from __future__ import annotations
from tools.roller import d6, flux, roll
from enum import Enum


class Starport(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    X = "X"

    @staticmethod
    def random() -> Starport:
        match roll():
            case r if r <= 4:
                return Starport.A
            case r if 4 < r <= 6:
                return Starport.B
            case r if 6 < r <= 8:
                return Starport.C
            case 9:
                return Starport.D
            case r if 9 < r < 12:
                return Starport.E
            case 12:
                return Starport.X
            case _:
                raise Exception("invalid roll")

    def tl_mod(self) -> int:
        match self.value:
            case "A":
                return 6
            case "B":
                return 4
            case "C":
                return 2
            case "X":
                return -4
            case _:
                return 0


class UWP:
    starport: Starport

    def __init__(self) -> None:
        self.starport = Starport.random()
        [self.size, self.population] = [roll() - 2, roll() - 2]

        self.atmosphere = max(0, self.size + flux())
        self.hydrographics = min(10, max(0, self.atmosphere + flux()))

        self.government = max(0, self.population + flux())
        self.law_level = max(0, self.government + flux())
        self.tech_level = max(0, d6() + self.starport.tl_mod())

    def __str__(self) -> str:
        return (
            f"{str(self.starport.value)}{self.size:01X}{self.atmosphere:01X}{self.hydrographics:01X}"
            f"{self.population:01X}{self.government:01X}{self.law_level:01X}-{self.tech_level:01X}"
        )
