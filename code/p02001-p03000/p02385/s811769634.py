import copy


class Dice:
    def __init__(self, eyes):
        self._eyes = ['dummy'] + eyes

    def __eq__(self, other):
        if other is None or not isinstance(other, Dice):
            return False

        # different left side patterns
        dups = []
        for _ in range(6):
            dups.append(copy.copy(self))
        dups[1].roll('W')
        dups[2].roll('SW')
        dups[3].roll('NW')
        dups[4].roll('E')
        dups[5].roll('WW')

        for dup in dups:
            for _ in range(4):
                dup.roll('N')
                if other.eyes == dup.eyes:
                    return True

        return False

    @property
    def eyes(self):
        return self._eyes[1:6]

    def roll(self, direction_text):
        for d in direction_text:
            self.roll_once(d)

    def roll_once(self, direction):
        a = self._eyes
        if direction == 'N':
            self._eyes = ['dummy', a[2], a[6], a[3], a[4], a[1], a[5]]
        elif direction == 'S':
            self._eyes = ['dummy', a[5], a[1], a[3], a[4], a[6], a[2]]
        elif direction == 'W':
            self._eyes = ['dummy', a[3], a[2], a[6], a[1], a[5], a[4]]
        elif direction == 'E':
            self._eyes = ['dummy', a[4], a[2], a[1], a[6], a[5], a[3]]
        else:
            raise ValueError('NEWS箱推し')


dice1 = Dice(input().split())
dice2 = Dice(input().split())
if dice1 == dice2:
    result = 'Yes'
else:
    result = 'No'
print(result)

