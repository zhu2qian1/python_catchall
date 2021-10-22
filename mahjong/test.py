from score_class import Score
from mahjong_constants import OYA, RON, KO, TSUMO

if __name__ == "__main__":
    ls = []
    ls.append(Score(4, 20, OYA, RON))
    ls.append(Score(4, 20, OYA, TSUMO))
    ls.append(Score(11, 40, OYA, RON))
    ls.append(Score(11, 40, OYA, TSUMO))
    ls.append(Score(13, 40, OYA, RON))
    ls.append(Score(13, 40, OYA, TSUMO))
    ls.append(Score(4, 40, KO, RON))
    ls.append(Score(4, 40, KO, TSUMO))
    ls.append(Score(11, 40, KO, RON))
    ls.append(Score(11, 40, KO, TSUMO))
    ls.append(Score(13, 40, KO, RON))
    ls.append(Score(13, 40, KO, TSUMO))

    print()
    [print(_, "\n") for _ in ls]
