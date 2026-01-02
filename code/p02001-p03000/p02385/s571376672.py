def main():
    labels1 = list(map(int, input().split(' ')))
    labels2 = list(map(int, input().split(' ')))

    dice1 = Dice(labels1)
    dice2 = Dice(labels2)

    print('Yes' if equals(dice1, dice2) else 'No')

def equals(d1, d2):
    for i in range(4):
        for j in range(4):
            if d1.equals(d2):
                return True
            d2.toE()
        d2.toN()

    d2.toE().toN()

    for i in range(2):
        for j in range(4):
            if d1.equals(d2):
                return True
            d2.toE()
        d2.toN().toN()

    return False

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

    def get_bottom(self):
        return self.labels[self._tb[1]]

    def get_front(self):
        return self.labels[self._fb[0]]

    def get_back(self):
        return self.labels[self._fb[1]]

    def get_left(self):
        return self.labels[self._lr[0]]

    def get_right(self):
        return self.labels[self._lr[1]]

    top    = property(get_top)
    bottom = property(get_bottom)
    front  = property(get_front)
    back   = property(get_back)
    left   = property(get_left)
    right  = property(get_right)

    def equals(self, other):
        if not (self.top == other.top and self.bottom == other.bottom):
            return False

        if not (self.front == other.front and self.back == other.back):
            return False

        if not (self.left == other.left and self.right == other.right):
            return False

        return True

    def __str__(self):
        return str([self.top, self.front, self.right, self.left, self.back, self.bottom])

if __name__ == '__main__':
    main()