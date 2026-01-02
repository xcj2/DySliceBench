from enum import IntEnum


class Position(IntEnum):
    TOP = 0
    FORESIDE = 1
    RIGHTSIDE = 2
    BACKSIDE = 3
    LEFTSIDE = 4
    BOTTOM = 5


class Dice:
    def __init__(self, v1, v2, v3, v4, v5, v6):
        self.values = {v1: [v1, v2, v3, v5, v4, v6],
                       v2: [v2, v6, v3, v1, v4, v5],
                       v3: [v3, v6, v5, v1, v2, v4],
                       v4: [v4, v6, v2, v1, v5, v3],
                       v5: [v5, v6, v4, v1, v3, v2],
                       v6: [v6, v5, v3, v2, v4, v1]}
        self.set_top(v1)

    def set_top(self, v):
        if v not in self.values:
            raise ValueError()

        self.top = v
        self.status = self.values[v]

    def rotate(self):
        (self.status[Position.FORESIDE], self.status[Position.RIGHTSIDE],
         self.status[Position.BACKSIDE], self.status[Position.LEFTSIDE]) \
         = (self.status[Position.LEFTSIDE], self.status[Position.FORESIDE],
            self.status[Position.RIGHTSIDE], self.status[Position.BACKSIDE])

    def __getitem__(self, side):
        return self.status[side]


def run():
    sides = [int(v) for v in input().split()]
    dice = Dice(*sides)
    cnt = int(input())

    for i in range(cnt):
        v1, v2 = [int(v) for v in input().split()]
        dice.set_top(v1)
        for j in range(4):
            if v2 == dice[Position.FORESIDE]:
                break
            dice.rotate()
        else:
            raise ValueError()

        print('{}'.format(dice[Position.RIGHTSIDE]))


if __name__ == '__main__':
    run()
