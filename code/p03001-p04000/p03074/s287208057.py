#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, S: str):
    d = []  # type: List[int]
    i = 0
    while True:
        r = 0
        while i < N and S[i] == "1":
            r += 1
            i += 1
        d.append(r)
        if i >= N:
            break
        s = 0
        while i < N and S[i] == "0":
            s += 1
            i += 1
        d.append(s)
    c = 2 * K + 1
    if c > len(d):
        print(sum(d))
        return
    dl = 0
    acc = sum(d[:c])
    ans = acc
    while dl + c + 2 <= len(d):
        acc += d[dl + c] + d[dl + c + 1] - d[dl] - d[dl + 1]
        ans = max(ans, acc)
        dl += 2
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)


if __name__ == '__main__':
    main()
