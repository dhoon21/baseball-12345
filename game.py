from game_result import GameResult

class Game:
    def __init__(self):
        self._question = ""
    
    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guessNumber) -> GameResult:
        if guessNumber is None:
            raise TypeError()

        if len(guessNumber) != 3:
            raise TypeError()

        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()

        if guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]:
            raise TypeError()

        return GameResult(True, 3, 0)