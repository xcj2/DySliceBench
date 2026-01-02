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

        self._top    = 0
        self._front  = 1
        self._right  = 2
        self._left   = 3
        self._back   = 4
        self._bottom = 5

    def toN(self):
        self._back, self._top, self._front, self._bottom = self._top, self._front, self._bottom, self._back
        return self

    def toS(self):
        self._back, self._top, self._front, self._bottom =  self._bottom, self._back, self._top, self._front
        return self

    def toW(self):
        self._left, self._top, self._right, self._bottom = self._top, self._right, self._bottom, self._left
        return self

    def toE(self):
        self._left, self._top, self._right, self._bottom = self._bottom, self._left, self._top, self._right
        return self

    def get_top(self):
        return self.labels[self._top]

    top = property(get_top)

if __name__ == '__main__':
    main()