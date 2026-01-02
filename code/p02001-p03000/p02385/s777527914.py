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

    def bottom(self):
        return self.d[5]

    def forTop(self, num):  #ある目がトップd[0]になるように回転させる。トップ以外の状態は知らん。
        for i in range(4):
            if self.top() == num:
                break
            self.e()
        else:
            for j in range(3):
                if self.top() == num:
                    break
                self.s()
    def same(self, dice):
        if self.d == dice.d:
            return True


def main():
    a_ = [int(i) for i in input().split()]
    b_ = [int(i) for i in input().split()]
    if not sorted(a_) == sorted(b_):
        print('No')
        return
    a = Dice(a_)
    b = Dice(b_)
    for i in range(4):
        for j in range(4):
            if b.same(a):
                print('Yes')
                return
            else:
                b.e()
        b.s()
    for i in range(4):
        for j in range(4):
            if b.same(a):
                print('Yes')
                return
            else:
                b.e()
        b.r()
    for i in range(4):
        for j in range(4):
            if b.same(a):
                print('Yes')
                return
            else:
                b.s()
        b.r()


    print('No')
    return




if __name__ == '__main__':
    main()

