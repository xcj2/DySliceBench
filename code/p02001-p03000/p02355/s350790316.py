#!/usr/bin/env python3
# DSL_3_B: The Smallest Window II


class Window:
    def __init__(self, k):
        self.k = k
        self.data = [0] * k
        self.zeros = set(range(k))

    def add(self, i):
        if self.data[i-1] == 0:
            self.zeros.remove(i-1)
        self.data[i-1] += 1

    def remove(self, i):
        if self.data[i-1] == 1:
            self.zeros.add(i-1)
        self.data[i-1] -= 1

    def removable(self, i):
        return self.data[i-1] > 1

    def open(self):
        return len(self.zeros) == 0


def run():
    n, k = [int(x) for x in input().split()]
    li = [int(x) for x in input().split()]
    w = Window(k)
    i = 0
    min_ = n+1
    for j, v in enumerate(li):
        if v <= k:
            w.add(v)
            while True:
                if li[i] > k:
                    pass
                elif w.removable(li[i]):
                    w.remove(li[i])
                else:
                    break
                i += 1
            if w.open():
                if min_ > j - i + 1:
                    min_ = j - i + 1

    if min_ > n:
        print(0)
    else:
        print(min_)


if __name__ == '__main__':
    run()

