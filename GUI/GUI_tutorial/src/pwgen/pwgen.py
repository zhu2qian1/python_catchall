#
#

pwspath: str = ".\\json\\pws\\pws.json"


def initialize(path: str) -> dict:
    """"""
    from json import load

    with open(path, encoding="utf8") as f:
        d: dict = load(f)
    return d


def finalize(path: str, obj: object) -> None:
    """"""
    from json import dump

    with open(path, mode="w", encoding="utf8") as f:
        dump(obj=obj, fp=f, ensure_ascii=False, indent=4)


def genpassword(ID: str = None, l: int = 8, punc: bool = True) -> dict:
    """
    Generate password under given conditions.
    Params
    --------
    ID: str
    l: int
    punc: bool
    Return
    --------
    tuple[ID, generated_pw]
    ID: str
    generated_pw: str
    """
    chars: list = []
    from random import choice
    from string import ascii_letters, digits

    chars.extend((ascii_letters * 2 + digits))
    if punc:
        from string import punctuation

        chars.extend(punctuation)

    return {ID: "".join([choice(chars) for _ in range(l)])}


d = initialize(pwspath)
gpw = genpassword
