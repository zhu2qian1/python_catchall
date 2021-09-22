from typing import Iterable
from compatibility_table import compatibility_table as compatibility_table
from compatibility_table import Table

compatibility_table: Table


def obtain_set_of_nemesises_of_enemy(
    name_of_enemy: str,
    compatibility_table: Table = compatibility_table,
    target_multiplication: str = "150",
) -> set[str]:

    try:
        info_of_enemy: list[str] = [
            i for i in compatibility_table if i[0] == name_of_enemy
        ][0]
    except IndentationError as e:
        raise e("Check the name of enemy.")

    # extract all the indices using enumerate
    positions: list[int] = [
        i for i, x in enumerate(info_of_enemy) if x == target_multiplication
    ]

    return set([compatibility_table[0][i] for i in positions])


def obtain_set_of_good_towers(enemies: Iterable[str]) -> set[str]:
    good_towers: set[str] = set()
    for i in enemies:
        good_towers |= obtain_set_of_nemesises_of_enemy(i)

    return good_towers


def imp_obtain_set_of_good_towers(enemies: Iterable[str]) -> dict:
    pass


if __name__ == "__main__":
    print(
        obtain_set_of_good_towers(
            ["regular", "fast", "toxic", "icy", "fighter", "boss"]
        )
    )
