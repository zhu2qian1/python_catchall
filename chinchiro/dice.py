class dice:
    def __init__(self) -> None:
        self.faces: tuple[str] = (1, 2, 3, 4, 5, 6)

    @staticmethod
    def roll(self) -> str:
        from random import choice

        return choice(self.faces)
