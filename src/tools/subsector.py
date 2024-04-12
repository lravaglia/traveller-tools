from tools.roller import d6
from tools.uwp import UWP


class Subsector:
    X: int = 1
    Y: int = 1
    W: int = 8

    worlds: list[tuple[str, UWP]] = []

    def __str__(self) -> str:
        ret = ""
        for (pos, uwp) in self.worlds:
            ret += f"{pos} {uwp}\n"
        return ret

    def __init__(self) -> None:
        x: int = self.X
        y: int = self.Y

        while y < self.Y + self.W:
            if d6() < 4:
                self.worlds.append((f"{x:02d}{y:02d}", UWP()))

            x += 1

            if x == self.W:
                y += 1
                x = self.X
