class Dice:
    def __init__(self, default = [1, 2, 3, 4, 5, 6]):
        self.d = default

    def e(self):
        self.d[0], self.d[2], self.d[3], self.d[5] = self.d[3], self.d[0], self.d[5], self.d[2]

    def w(self):
        self.d[0], self.d[2], self.d[3], self.d[5] = self.d[2], self.d[5], self.d[0], self.d[3]

    def n(self):
        self.d[0], self.d[1], self.d[4], self.d[5] = self.d[1], self.d[5], self.d[0], self.d[4]

    def s(self):
        self.d[0], self.d[1], self.d[4], self.d[5] = self.d[4], self.d[0], self.d[5], self.d[1]

    def top(self):
        return self.d[0]


def main():
    dice = Dice([int(i) for i in input().split()])
    for o in input():
        if o == 'E':
            dice.e()
        elif o == 'W':
            dice.w()
        elif o == 'S':
            dice.s()
        else:
            dice.n()

    print(dice.top())


if __name__ == '__main__':
    main()





