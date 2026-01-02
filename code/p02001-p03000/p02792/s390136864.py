#!/usr/bin/env python3
import itertools
import sys


def solve(N: int):
    sN = str(N)
    lN = len(sN)
    if lN == 1:
        print(N)
        return
    l1 = int(sN[0])
    l2 = int(sN[-1])
    d = {}
    for k1, k2 in itertools.product(range(1, 10), repeat=2):
        p = 10 ** (lN - 2) // 9
        if k1 == k2:
            p += 1
        if k1 < l1:
            p += 10 ** (lN - 2)
        elif k1 == l1:
            p += int(sN[1:-1] or "0")
            if k2 <= l2:
                p += 1
        d[k1, k2] = p

    ans = 0
    for k1, k2 in itertools.product(range(1, 10), repeat=2):
        ans += d[k1, k2] * d[k2, k1]
    print(ans)


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
