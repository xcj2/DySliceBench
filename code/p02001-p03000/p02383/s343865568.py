from enum import IntEnum


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Dice:
    """Dice class implements the structure of a dice
    having six faces.
    """
    def __init__(self, v1, v2, v3, v4, v5, v6):
        self.top = 1
        self.heading = Direction.NORTH
        self.values = [v1, v2, v3, v4, v5, v6]

    def to_dice_axis(self, d):
        return (d - self.heading) % 4

    def to_plain_axis(self, d):
        return (self.heading + d) % 4

    def roll(self, d):
        faces = [[(2, Direction.NORTH), (6, Direction.NORTH),
                  (6, Direction.WEST), (6, Direction.EAST),
                  (6, Direction.SOUTH), (5, Direction.SOUTH)],
                 [(4, Direction.EAST), (4, Direction.NORTH),
                  (2, Direction.NORTH), (5, Direction.NORTH),
                  (3, Direction.NORTH), (4, Direction.WEST)],
                 [(5, Direction.SOUTH), (1, Direction.NORTH),
                  (1, Direction.EAST), (1, Direction.WEST),
                  (1, Direction.SOUTH), (2, Direction.NORTH)],
                 [(3, Direction.WEST), (3, Direction.NORTH),
                  (5, Direction.NORTH), (2, Direction.NORTH),
                  (4, Direction.NORTH), (3, Direction.EAST)]]
        f, nd = faces[self.to_dice_axis(d)][self.top-1]
        self.top = f
        self.heading = self.to_plain_axis(nd)

    def value(self):
        return self.values[self.top-1]


def run():
    values = [int(v) for v in input().split()]
    dice = Dice(*values)
    for d in input():
        if d == 'N':
            dice.roll(Direction.NORTH)
        if d == 'E':
            dice.roll(Direction.EAST)
        if d == 'S':
            dice.roll(Direction.SOUTH)
        if d == 'W':
            dice.roll(Direction.WEST)

    print(dice.value())


if __name__ == '__main__':
    run()

