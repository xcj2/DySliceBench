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

    def r(self):
        self.d[1], self.d[2], self.d[3], self.d[4] = self.d[3], self.d[1], self.d[4], self.d[2]

    def top(self):
        return self.d[0]

    def forward(self):
        return self.d[1]

    def right(self):
        return self.d[2]


def main():
    dice = Dice([int(i) for i in input().split()])
    n = int(input())
    for i in range(n):
        t, f = map(int, input().split())
        for i in range(4):
            if dice.top() == t:
                break
            dice.e()
        else:
            for j in range(3):
                if dice.top() == t:
                    break
                dice.s()

        for i in range(3):
            if dice.forward() == f:
                break
            dice.r()

        print(dice.right())


if __name__ == '__main__':
    main()

