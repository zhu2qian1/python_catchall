from random import choice
from data import kiseki_taiken as kt, unbelievable as ub
from sys import argv


def main(*args) -> None:
    try:
        for _ in range(int(args[1])):
            print(shuffle())
    except ValueError:
        print(shuffle())
    except IndexError:
        print(shuffle())


def shuffle() -> str:
    ki_tai: str = "".join((choice(kt) for i in range(4)))
    an_bo: str = "".join((choice(ub) for i in range(6)))

    return f"{ki_tai}！{an_bo}ー"


if __name__ == "__main__":
    main(*argv)
