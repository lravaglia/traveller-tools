from tools.roller import d6, flux, roll

class UWP:
    def __init__(self) -> None:
        self.starport = "A"
        [self.size, self.population] = [roll() - 2, roll() - 2]

        self.atmosphere = max(0, self.size + flux())
        self.hydrographics = min(10, max(0, self.atmosphere + flux()))

        self.government = max(0, self.population + flux())
        self.law_level = max(0, self.government + flux())

    def __str__(self) -> str:
        return (
            f"{self.starport}{ehex(self.size)}{ehex(self.atmosphere)}{ehex(self.hydrographics)}"
            f"{ehex(self.population)}{ehex(self.government)}{ehex(self.law_level)}-{ehex(d6())}"
        )

def ehex(num: int) -> str:
    assert(num >= 0)

    if num < 10:
        return str(num)
    else:
        return chr(45 + num)
