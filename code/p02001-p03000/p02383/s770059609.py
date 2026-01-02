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
    cmd = list(input())
    for c in cmd:
        if c == 'N':
            dice.north()
        elif c == 'W':
            dice.west()
        elif c == 'E':
            dice.east()
        elif c == 'S':
            dice.south()
    print(dice.label[0])


if __name__ == '__main__':
    main()