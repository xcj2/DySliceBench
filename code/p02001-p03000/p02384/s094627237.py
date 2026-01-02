import sys
input = sys.stdin.readline


class Dice:
    """
    0:top, 1:south, 2:east, 3:west, 4:north, 5:bottom
    """

    def __init__(self, surfaces):
        self.init_surface = surfaces
        self.surface = surfaces

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
        return self.surface.index(num)

    def get_top(self):
        return self.surface[0]

    def get_south(self):
        return self.surface[1]

    def get_east(self):
        return self.surface[2]


def main():
    surface = [int(i) for i in input().strip().split()]
    cases = int(input().strip())
    dice = Dice(surface)

    for _ in range(cases):
        top, south = [int(i) for i in input().strip().split()]
        # get current surface
        cur = dice.get_surface(top)
        if cur == 0:
            pass
        elif cur == 1:
            dice.roll("N")
        elif cur == 2:
            dice.roll("W")
        elif cur == 3:
            dice.roll("E")
        elif cur == 4:
            dice.roll("S")
        elif cur == 5:
            dice.roll("S")
            dice.roll("S")
        for _ in range(4):
            dice.spin()
            if dice.get_south() == south:
                print(dice.get_east())


if __name__ == "__main__":
    main()

