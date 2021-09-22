class GameUtil:
    def yes_or_no_question(self, prompt: str) -> bool:
        while True:
            i = input()
            if i in ("n", "N", "No", "no"):
                return False
            elif i in ("y", "Y", "Yes", "yes"):
                return True
            else:
                print("Enter a valid answer.")


class JankenGameBase:
    def __init__(self) -> None:

        self.hands = {
            0: "rock",
            1: "scissor",
            2: "paper",
        }
        self.colors = {
            0: "magenta",
            1: "yellow",
            2: "cyan",
        }


class JankenGame(JankenGameBase, GameUtil):
    def __init__(self):
        super().__init__()

    def game(self) -> tuple:
        "return opponent_hand: int, player_hand: int"

        from random import randint

        while 1:
            print("0: rock, 1: scissor, 2: paper")
            try:
                player_hand = int(input("Choose your hand >>> "))
                # Validation
                if player_hand not in (0, 1, 2):
                    raise ValueError
            except ValueError:
                print("Enter a valid answer.")

        return randint(0, 2), player_hand

    def judge(self, result: tuple) -> int:
        "judge a game."
        if result[0] == result[1]:
            # draw
            return 0
        elif (result[0] - result[1] + 3) % 3 == 1:
            # player won
            return 1
        else:
            # player lost
            return -1

    def mainloop(self):
        "mainloop."
