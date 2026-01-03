#!/usr/bin/env python3
import sys
from collections import deque
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, S: "List[str]"):

    counter = 1
    s1, s2 = S
    pre = 0
    i = 0
    while i < N:
        if s1[i] == s2[i]:
            counter *= 3-pre
            counter %= MOD
            i += 1
            pre = 1
        else:
            if pre == 0:
                counter *= 6
                counter %= MOD
            elif pre == 1:
                counter *= 2
                counter %= MOD
            else:
                counter *= 3
                counter %= MOD

            i += 2
            pre = 2

    print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(2)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
