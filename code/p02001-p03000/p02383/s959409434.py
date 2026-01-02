class Dice:
    def __init__(self, eyes):
        self._eyes = ['dummy'] + eyes

    @property
    def eye(self):
        return self._eyes[1]

    def roll(self, direction):
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


eyes = input().split()
dice = Dice(eyes)

direction_text = input()
for d in direction_text:
    dice.roll(d)

print(dice.eye)

