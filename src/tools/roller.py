from random import randint


def d6() -> int:
    return randint(1, 6)

def roll() -> int:
    return d6() + d6()

def flux() -> int:
    return d6() - d6()
