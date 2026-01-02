#!/usr/bin/env python3
import sys
from itertools import accumulate
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


def inversion(a):
    "転倒していない組(l, r)の個数を求める"
    d = {av: i+1 for i, av in enumerate(sorted(a))}
    b = Bit(len(a))
    ans = 0
    for i, av in enumerate(a):
        ans += b.sum(d[av])
        b.add(d[av], 1)
    return ans


def solve(N: int, a: "List[int]"):

    def isOK(y):
        acc = (1 if aa >= y else -1 for aa in a)
        acc = tuple([0]) + tuple(accumulate(acc))
        invs = inversion(acc)
        if acc[0] == -1:
            invs -= 1
        return invs < (N*(N+1))//4

    def binary_search(x):

        ng = -1
        ok = len(x)+1

        while abs(ok - ng) > 1:
            mid = (ok + ng)//2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ng, ok

    ng, ok = binary_search(range(max(a)))
    print(ng)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
