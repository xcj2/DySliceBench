
import sys
input = sys.stdin.readline


class Dice:
    """
    0:top, 1:south, 2:east, 3:west, 4:north, 5:bottom
    """

    def __init__(self, surfaces):
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

    def get_top(self):
        return self.surface[0]


def main():
    surface = [int(i) for i in input().strip().split()]
    spins = input().strip()
    dice = Dice(surface)
    for d in spins:
        dice.roll(d)
    print(dice.get_top())


if __name__ == "__main__":
    main()
