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

    def same_rotate(self, dice):
        saved_d = self.d[:]
        for i in range(4):
            for j in range(4):
                if self.same(dice):
                    self.d = saved_d
                    return True
                else:
                    self.e()
            self.s()
        for i in range(4):
            for j in range(4):
                if self.same(dice):
                    self.d = saved_d
                    return True
                else:
                    self.e()
            self.r()
        for i in range(4):
            for j in range(4):
                if self.same(dice):
                    self.d = saved_d
                    return True
                else:
                    self.s()
            self.r()
        self.d = saved_d
        return False



def main():
    n = int(input())
    data = [Dice(list(map(int, input().split()))) for _ in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if data[i].same_rotate(data[j]):
                print('No')
                return

    print('Yes')
    return





if __name__ == '__main__':
    main()





