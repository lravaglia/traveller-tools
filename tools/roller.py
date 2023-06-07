from random import randint


def d6() -> int:
    return randint(1, 6)


def roll() -> int:
    return d6() + d6()


def flux() -> int:
    return d6() - d6()


if __name__ == "__main__":
    s = roll() - 2
    a = s + flux()
    h = a + flux()

    p = roll() - 2
    g = p + flux()
    l = g + flux()

    print(f"{s} {a} {h}  {p} {g} {l}")
