#!/usr/bin/env python3

import sys, math
sys.setrecursionlimit(300000)


def solve(N: int):
    n = math.ceil(N ** 0.5)
    ret = [0] * (N + 1)
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                s = x * x + y * y + z * z + x * y + y * z + z * x
                if 1 <= s <= N:
                    ret[s] += 1
    for i in range(N):
        print(ret[i + 1])
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
