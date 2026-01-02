# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/11/ITP1_11_A


class Dice(object):
    def __init__(self, top, front, right, left, back, bottom):
        self.t = top
        self.f = front
        self.r = right
        self.l = left
        self.bc = back
        self.bt = bottom

    def roll(self, direction):
        if direction == 'N':
            self.t, self.f, self.bt, self.bc = self.f, self.bt, self.bc, self.t
        elif direction == 'S':
            self.t, self.f, self.bt, self.bc = self.bc, self.t, self.f, self.bt
        elif direction == 'E':
            self.t, self.l, self.bt, self.r = self.l, self.bt, self.r, self.t
        elif direction == 'W':
            self.t, self.l, self.bt, self.r = self.r, self.t, self.l, self.bt

    def show_top(self):
        print(self.t)

    def __str__(self):
        # top, front, right, left, back, bottom
        return f'{self.t}, {self.f}, {self.r}, {self.l}, {self.bc}, {self.bt}'


def solve():
    dice = Dice(*input().split())

    for direction in input():
        dice.roll(direction)
    dice.show_top()


if __name__ == '__main__':
    solve()

