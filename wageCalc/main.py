class WageCalcBase:
    def __init__(
        self, base_wage: float, num_bonus: int, assesment_factor: float = 1.0
    ) -> None:
        "base for WageCalc."
        self.base_wage: float = base_wage
        self.num_bonus: int = num_bonus
        self.assesment_factor: float = assesment_factor

    def calc_yearly_salary(self) -> float:
        ""
        return (
            self.base_wage * 12 + self.base_wage * 2 * self.num_bonus
        ) * self.assesment_factor

    def calc_tedori(self) -> float:
        return self.calc_yearly_salary() / 12 * 0.8


class WageCalc(WageCalcBase):
    def __init__(
        self, base_wage: float, num_bonus: int, assesment_factor: float
    ) -> WageCalcBase:
        super(WageCalc, self).__init__(base_wage, num_bonus, assesment_factor)


w = WageCalc(21.0, 1, 1)
print(w.calc_yearly_salary())
print(w.calc_tedori())
