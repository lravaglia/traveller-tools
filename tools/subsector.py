from tools.roller import d6
from tools.uwp import UWP


Position = tuple[int, int]


class Subsector:
    X: int = 1
    Y: int = 1
    W: int = 8

    @classmethod
    def random(cls) -> list[tuple[Position, UWP]]:
        worlds: list[tuple[Position, UWP]] = []
        x: int = cls.X
        y: int = cls.Y

        while y < cls.Y + cls.W:
            if d6() < 4:
                worlds.append(((x, y), UWP()))

            x += 1

            if x == cls.W:
                y += 1
                x = cls.X

        return worlds
