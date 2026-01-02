def main():
    labels = list(map(int, input().split(' ')))

    n = int(input())

    for i in range(n):
        dice = Dice(labels)
        t, f = map(int, input().split(' '))

        for j in range(8):
            if j%4 == 0:
                dice.toE()

            if f == dice.front:
                break

            dice.toN()

        for j in range(4):
            if t == dice.top:
                break
            dice.toE()

        print(dice.right)

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

    def get_front(self):
        return self.labels[self._fb[0]]

    def get_right(self):
        return self.labels[self._lr[1]]

    top   = property(get_top)
    front = property(get_front)
    right = property(get_right)

if __name__ == '__main__':
    main()