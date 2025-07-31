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

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)

        if guess_number == self._question:
            return GameResult(True, 3, 0)

        return GameResult(False, 0, 0)

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError()
        if len(guess_number) != 3:
            raise TypeError()
        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if guess_number[0] == guess_number[1] or \
                guess_number[0] == guess_number[2] or \
                guess_number[1] == guess_number[2]:
            raise TypeError()

