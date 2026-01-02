# coding: utf-8


class BinaryIndexedTree(object):
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (N + 1)

    def add(self, a, w):
        x = a
        while x <= self.N:
            self.tree[x] += w
            x += (x & -x)

    def sum(self, a):
        if a == 0:
            return 0
        s = 0
        x = a
        while x > 0:
            s += self.tree[x]
            x -= (x & -x)
        return s


def main():
    N, Q = map(int, input().split(" "))
    bit = BinaryIndexedTree(N)
    for i in range(Q):
        c, x, y = map(int, input().split(" "))
        if c == 0:
            bit.add(x, y)
            # print(bit.tree)
        elif c == 1:
            print(bit.sum(y) - bit.sum(x-1))



if __name__ == "__main__":
    main()