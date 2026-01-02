#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, C: int, s: "List[int]", t: "List[int]", c: "List[int]"):
    progs = [[] for _ in range(C)]
    for si, ti, ci in zip(s, t, c):
        progs[ci - 1].append((si, ti))
    ds = []
    for prog in progs:
        if not prog:
            continue
        prog.sort()
        ds.append((prog[0][0] - 1, 1))
        ds.append((prog[-1][1], -1))
        for i in range(len(prog) - 1):
            if prog[i][1] != prog[i + 1][0]:
                ds.append((prog[i][1], -1))
                ds.append((prog[i + 1][0] - 1, 1))
    ds.sort()
    ans = 0
    m = 0
    for _, d in ds:
        m += d
        ans = max(ans, m)
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    s = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, s, t, c)


if __name__ == '__main__':
    main()
