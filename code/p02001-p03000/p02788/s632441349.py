#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def solve(N: int, D: int, A: int, X: "List[int]", H: "List[int]"):

    bit = Bit(N+1)

    XH = [(x, h) for x, h in zip(X, H)]
    XH.sort()
    for i in range(N):
        if i == 0:
            bit.add(i+1, XH[i][1])
        else:
            bit.add(i+1, XH[i][1]-XH[i-1][1])
    # print(XH)

    tot = 0
    curr = 0
    while True:
        # Hが正であるうち、xが最も小さいxhを見つける すべてでO(N)
        # print([bit.sum(i+1) for i in range(N)])

        flag = False
        for i in range(curr, N):
            if bit.sum(i+1) > 0:
                flag = True
                break
        if flag:
            curr = i+1
        else:
            break
        # できるだけ多くを巻き込むようにバクダンを使う。 x ~ x+2D
        x, h = XH[i]
        h = bit.sum(i+1)
        kaisu = -(-h//A)
        damage = A*kaisu
        tot += kaisu

        # 巻き込むモンスターは i ~ jまで
        j = bisect_left(XH, (x+2*D+1, 0))
        bit.add(i+1, -damage)
        bit.add(j+1, +damage)
        # for k in range(i, j):
        #     x, h = XH[k]
        #     XH[k] = (x, h-damage)
    print(tot)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    H = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        H[i] = int(next(tokens))
    solve(N, D, A, X, H)


if __name__ == '__main__':
    main()
