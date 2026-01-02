import copy


class Dice:
    def __init__(self, eyes):
        self._top = eyes[0]
        self._front = eyes[1]
        self._right = eyes[2]
        self._left = eyes[3]
        self._back = eyes[4]
        self._bottom = eyes[5]

    @property
    def eye(self):
        return self._top

    def roll(self, direction):
        old = copy.copy(self)
        if direction == 'N':
            self._top = old._front
            self._front = old._bottom
            self._back = old._top
            self._bottom = old._back
        elif direction == 'S':
            self._top = old._back
            self._front = old._top
            self._back = old._bottom
            self._bottom = old._front
        elif direction == 'W':
            self._top = old._right
            self._right = old._bottom
            self._left = old._top
            self._bottom = old._left
        elif direction == 'E':
            self._top = old._left
            self._right = old._top
            self._left = old._bottom
            self._bottom = old._right
        else:
            raise ValueError('NEWS箱推し')


eyes = input().split()
dice = Dice(eyes)

direction_text = input()
for d in direction_text:
    dice.roll(d)

print(dice.eye)

