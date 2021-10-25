from Score_calculator import calc_final_score, make_prefix, make_suffix


class Score:
    def __init__(self, han: int, fu: int, is_oya: bool, is_ron: bool):
        self.han = han
        self.fu = fu
        self.oya_or_ko = "親" if is_oya else "子"
        self.ron_or_tsumo = "ロン" if is_ron else "ツモ"
        self.string_score: str
        final_score = calc_final_score(han, fu, is_oya, is_ron)

        if type(final_score) == int:
            self.string_score = str(final_score)
        else:  # ツモ
            if is_oya:  # 親のツモ
                self.string_score = str(final_score[0])
            else:
                self.string_score = (
                    f"{final_score[0]}-{final_score[1]}"  # 1000-2000 みたいな形
                )

        self.prefix = make_prefix(han, fu)
        self.suffix = make_suffix(is_oya, is_ron)

    def __str__(self):
        return f"{self.oya_or_ko} {self.ron_or_tsumo} {self.han}翻 {self.fu}符\n{self.prefix}{self.string_score}{self.suffix}"
