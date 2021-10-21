def make_prefix(han: int, fu: int) -> str:
    """満貫とか倍満とか点数の前に言うやつを生成する。

    Args:
        han (int): 翻数。
        fu (int): 符数。

    Returns:
        str: 翻数と符数に応じて「満貫」とか「三倍満」とかの文字列を返す。
    """
    if han >= 13:
        return "数え役満 "
    if han >= 11:
        return "三倍満 "
    if han >= 8:
        return "倍満 "
    if han >= 6:
        return "跳満 "
    if han >= 5:
        return "満貫 "
    if han == 4 and fu >= 30:
        return "満貫 "
    if han == 3 and fu >= 60:
        return "満貫 "
    return ""


def make_suffix(is_oya: bool, is_ron: bool) -> str:
    """～点とか～オールみたいな点数の後につけるやつを生成する。

    Args:
        is_oya (bool): 親かどうか。
        is_ron (bool): ロンかどうか。

    Returns:
        str: ～点 とか ～オール みたいな点数の後にくっつける文字列を返す。

    """
    if is_ron:
        return "点"
    if not is_ron and is_oya:
        return "オール"
    return ""


def calc_final_score(han: int, fu: int, is_oya: bool, is_ron: bool):
    base_score = calc_base_score(han, fu)
    if is_ron:
        return calc_score_of_ron(base_score, is_oya)
    return calc_score_of_tsumo(base_score, is_oya)


def calc_score_of_tsumo(base_score: int, is_oya: bool) -> tuple[int]:
    if is_oya:
        return ceil_score(base_score * 2), ceil_score(base_score * 2)  # 親のツモ
    return ceil_score(base_score), ceil_score(base_score * 2)  # 子のツモ


def calc_score_of_ron(base_score: int, is_oya: bool) -> int:
    if is_oya:
        return ceil_score(base_score * 6)
    return ceil_score(base_score * 4)


def calc_base_score(han: int, fu: int, kiriage_mangan: bool = True) -> int:
    """与えられた翻数と符から基本点を計算する。

    Args:
        han (int):
            翻数。場ゾロは含めない。
            5翻で満貫、6, 7翻で跳満、8, 9, 10翻で倍満、11, 12 翻で三倍満、13翻以上で数え役満とする。

        fu (int):
            符数。切り上げ前のもので良い。25が与えられたら25を返す（七対子）。

        kiriage_mangan (bool, optional):
            切り上げ満貫の有無。4翻30符、3翻60符の場合は切り上げ満貫とするか。Defaults to True.

    Returns:
        int: 基本点。
    """

    if han >= 13:
        return 8000
    if han >= 11:
        return 6000
    if han >= 8:
        return 4000
    if han >= 6:
        return 3000
    if han >= 5:
        return 2000
    if han == 4 and fu >= 30:
        return 2000
    if han == 3 and fu >= 60:
        return 2000

    return ceil_fu(fu) * pow(2, han + 2)


def ceil_fu(fu: int) -> int:
    """切り上げ前の符から得点計算に使う符を返す。25が与えられたら25を返す（七対子）。

    Args:
        fu (int): 切り上げ前の符。

    Returns:
        int: 得点計算に使う符。
    """
    if fu == 25:
        return 25  # 七対子
    return ceil_with_base(fu, 10)


def ceil_score(score):
    return ceil_with_base(score, 100)


def ceil_with_base(num: int, base: int) -> int:
    if num % base == 0:
        return num
    return (num // base) * base + base
