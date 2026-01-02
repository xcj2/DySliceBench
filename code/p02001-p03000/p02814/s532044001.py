#!/usr/bin/env python3
import sys
import math
from functools import reduce
import operator
INF = float("inf")


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def LCM(a, b):
    return a*b//GCD(a, b)


def solve(N: int, M: int, a: "List[int]"):

    # 各aを2で割れる回数(の２べき)
    K = set()
    for i, av in enumerate(a):
        K.add(av & -av)
    if len(K) != 1:
        print(0)
        return

    lcm = a[0]//2
    for av in a:
        lcm = LCM(lcm, av//2)

    ans = int(M/lcm)
    if ans > 0 and ans % 2 == 0:
        ans -= 1
    ans = (ans+1)//2

    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, a)


if __name__ == '__main__':
    main()
