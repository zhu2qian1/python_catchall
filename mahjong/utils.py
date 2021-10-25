from typing import TypeAlias
from random import shuffle, seed

tuple_str: TypeAlias = tuple[str]


def make_char_arr(s: str) -> tuple[str]:
    return tuple([_ for _ in s])


def is_penchan(s: str, kanji_mode=True) -> bool:
    penchan: str = "二三四五六七八" if kanji_mode else "2345678"
    for p in penchan:
        if p in s:
            return True
    return False


def is_yaochu(s: str, kanji_mode=True) -> bool:
    penchan: str = "二三四五六七八" if kanji_mode else "2345678"
    for p in penchan:
        if p in s:
            return False
    return True


def create_paiset(pais: tuple_str) -> list:
    return [*pais * 4]


def shuffle_paiset(pais: list, seed_val=None) -> None:
    if seed_val is None:
        shuffle(pais)
    seed(seed_val)
    shuffle(pais)


# ----
KANSUJI: tuple_str = tuple_str("一二三四五六七八九")

A_NUMBERS: tuple_str = tuple_str("123456789")

# ----
JIHAI: tuple_str = tuple_str("東南西北白發中")
MANZU: tuple_str = tuple(f"{i}萬" for i in KANSUJI)
SOZU: tuple_str = tuple(f"{i}索" for i in KANSUJI)
PINZU: tuple_str = tuple(f"{i}筒" for i in KANSUJI)

A_JIHAI: tuple_str = tuple(f"{i}z" for i in range(1, 8))
A_MANZU: tuple_str = tuple(f"{i}m" for i in A_NUMBERS)
A_SOZU: tuple_str = tuple(f"{i}s" for i in A_NUMBERS)
A_PINZU: tuple_str = tuple(f"{i}p" for i in A_NUMBERS)

# ----
ALLKINDS: tuple_str = tuple([*JIHAI, *MANZU, *SOZU, *PINZU])

A_ALLKINDS: tuple_str = tuple([*A_JIHAI, *A_MANZU, *A_SOZU, *A_PINZU])

# ----
YAOCHUS: tuple_str = tuple(filter(is_yaochu, ALLKINDS))
PENCHANS: tuple_str = tuple(filter(is_penchan, ALLKINDS))

A_YAOCHUS: tuple_str = tuple([x for x in A_ALLKINDS if is_yaochu(x, kanji_mode=False)])
A_PENCHANS: tuple_str = tuple(
    [x for x in A_ALLKINDS if is_penchan(x, kanji_mode=False)]
)

# ----
IWAN: str = "一萬"
CHUWAN: str = "九萬"

A_IWAN: str = "1m"
A_CHUWAN: str = "9m"

# ----
SANMA_PAIS: tuple_str = tuple([*SOZU, *PINZU, *JIHAI, IWAN, CHUWAN])
YONMA_PAIS: tuple_str = ALLKINDS

A_SANMA_PAIS: tuple_str = tuple(
    [*A_SOZU, *A_PINZU, *A_MANZU, *A_JIHAI, A_IWAN, A_CHUWAN]
)
A_YONMA_PAIS: tuple_str = A_ALLKINDS

# ----
WINDS: tuple_str = tuple([f"{i}家" for i in "東南西北"])
WINDS_SANMA: tuple_str = tuple([f"{i}家" for i in "東南西"])

A_WINDS: tuple_str = "East", "South", "West", "North"
A_WINDS_SANMA: tuple_str = "East", "South", "West"

# ----
SUITE_NUMBER: dict[str, int] = {"z": 0, "m": 10, "s": 20, "p": 30}


def fetch_pai_value(pai: str) -> int:
    return int(pai[0]) + SUITE_NUMBER[pai[1]]
