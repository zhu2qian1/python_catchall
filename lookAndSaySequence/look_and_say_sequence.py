from typing import Union


def read_aloud(sequence: tuple) -> tuple:
    "look at a sequence and read aloud."
    if sequence == (1,):
        return (1, 1)

    number = sequence[0]
    in_row = 1
    stack = []
    for i in sequence[1:]:
        if number == i:
            in_row += 1
        else:
            stack.append(in_row)
            stack.append(number)
            in_row = 1
            number = i

    stack.append(in_row)
    stack.append(number)
    return tuple(stack)


def look_and_say_sequence(length: int) -> tuple:
    "return look and say sequence to 'length'."
    if length == 1:
        return read_aloud((1,))
    else:
        return read_aloud(look_and_say_sequence(length - 1))


if __name__ == "__main__":
    from pprint import pprint as pp
    from sys import argv

    pp(look_and_say_sequence(int(argv[1])))
