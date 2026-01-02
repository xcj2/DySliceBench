import random


class Dice():

    def __init__(self, label):
        self.label = label

    def north(self):
        self.change([2, 6, 3, 4, 1, 5])

    def west(self):
        self.change([3, 2, 6, 1, 5, 4])

    def east(self):
        self.change([4, 2, 1, 6, 5, 3])

    def south(self):
        self.change([5, 1, 3, 4, 6, 2])

    def change(self, convert):
        num = []
        for i in range(6):
            num.append(self.label[convert[i] - 1])
        self.label = num


def main():
    dice = Dice([int(x) for x in input().split()])
    n = int(input())
    for i in range(n):
        upper, front = [int(x) for x in input().split()]
        while dice.label[0] != upper or dice.label[1] != front:
            direction = random.randint(0, 3)
            if direction == 0:
                dice.north()
            elif direction == 1:
                dice.west()
            elif direction == 2:
                dice.east()
            elif direction == 3:
                dice.south()
        print(dice.label[2])


if __name__ == '__main__':
    main()