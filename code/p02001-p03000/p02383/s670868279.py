def main():
    nums = list(map(int, input().split(' ')))
    directs = input()

    d = Dice(nums)

    for c in directs:
        if 'N' == c:
            d.toN()

        if 'S' == c:
            d.toS()

        if 'E' == c:
            d.toE()

        if 'W' == c:
            d.toW()

    print(d.top)

class Dice:
    def __init__(self, labels):
        self.labels = labels

        self._tb = (0, 5)
        self._fb = (1, 4)
        self._lr = (3, 2)

    def toN(self):
        tb = self._tb
        self._tb = self._fb
        self._fb = tuple(reversed(tb))

        return self

    def toS(self):
        tb = self._tb
        self._tb = tuple(reversed(self._fb))
        self._fb = tb

        return self

    def toW(self):
        tb = self._tb
        self._tb = tuple(reversed(self._lr))
        self._lr = tb

        return self

    def toE(self):
        tb = self._tb
        self._tb = self._lr
        self._lr = tuple(reversed(tb))

        return self

    def get_top(self):
        return self.labels[self._tb[0]]

    top = property(get_top)

if __name__ == '__main__':
    main()