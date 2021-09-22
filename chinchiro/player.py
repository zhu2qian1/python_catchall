class player:

    number: int = 0

    def __init__(self) -> None:
        self.number += 1

        self.id: int = self.number
        self.money: int = 10000

    def __str__(self) -> str:
        return f"Id: {self.id}, Money: {self.money}"

    def bet(self, bet: int) -> None:
        self.money -= bet

    def win(self, amount: int) -> None:
        self.money += amount
