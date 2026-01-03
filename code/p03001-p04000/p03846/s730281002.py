#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    c = Counter(A)
    flag = True
    if N % 2 == 0:
        for i in range(1, N, 2):
            if c[i] != 2:
                flag = False
        if flag == False:
            print(0)
            return
    else:
        for i in range(0, N, 2):
            if i == 0:
                if c[i] != 1:
                    flag = False
            elif c[i] != 2:
                flag = False
        if flag == False:
            print(0)
            return
    print(pow(2, N//2, MOD))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
