import sys
input = sys.stdin.readline


class Dice:
    """
    0:top, 1:south, 2:east, 3:west, 4:north, 5:bottom
    """

    def __init__(self, surfaces):
        self.init_surface = surfaces
        self.surface = surfaces

    def init_dice(self):
        self.surface = self.init_surface

    def roll(self, direction: str):
        if direction == "E":
            self.surface = [self.surface[3], self.surface[1], self.surface[0],
                            self.surface[5], self.surface[4], self.surface[2]]

        elif direction == "N":
            self.surface = [self.surface[1], self.surface[5], self.surface[2],
                            self.surface[3], self.surface[0], self.surface[4]]

        elif direction == "S":
            self.surface = [self.surface[4], self.surface[0], self.surface[2],
                            self.surface[3], self.surface[5], self.surface[1]]

        elif direction == "W":
            self.surface = [self.surface[2], self.surface[1], self.surface[5],
                            self.surface[0], self.surface[4], self.surface[3]]

        return

    def spin(self):
        self.surface = [self.surface[0], self.surface[3], self.surface[1],
                        self.surface[4], self.surface[2], self.surface[5]]
        return

    def get_surface(self, num):
        if num in self.surface:
            indexes = [i for i, x in enumerate(self.surface) if x == num]
            return indexes
        else:
            return None

    def get_top(self):
        return self.surface[0]

    def get_south(self):
        return self.surface[1]

    def get_east(self):
        return self.surface[2]


def main():
    surface = [int(i) for i in input().strip().split()]
    dice1 = Dice(surface)
    surface = [int(i) for i in input().strip().split()]
    dice2 = Dice(surface)

    top1 = dice1.get_top()
    indexes = dice2.get_surface(top1)
    for cur in indexes:
        dice2.init_dice()
        if cur == 0:
            pass
        elif cur == 1:
            dice2.roll("N")
        elif cur == 2:
            dice2.roll("W")
        elif cur == 3:
            dice2.roll("E")
        elif cur == 4:
            dice2.roll("S")
        elif cur == 5:
            dice2.roll("S")
            dice2.roll("S")
        for _ in range(4):
            dice2.spin()
            if dice1.surface == dice2.surface:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()

