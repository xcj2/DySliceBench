#!/usr/bin/env python3

import sys, bisect
sys.setrecursionlimit(300000)

def solve(N: int, S: str):
    tmp = {'R': [], 'G': [], 'B': []}
    for i, c in enumerate(S):
        tmp[c].append(i)

    ret = 0
    x = len(tmp['R'])
    y = len(tmp['G'])
    z = len(tmp['B'])
    ret = x * y * z
    for r in tmp['R']:
        for g in tmp['G']:
            d = abs(g - r)
            if g > r:
                t = g + d
            else:
                t = r + d
            idx = bisect.bisect_left(tmp['B'], t)
            if idx < z and tmp['B'][idx] == t:
                ret -= 1
    for r in tmp['R']:
        for b in tmp['B']:
            d = abs(b - r)
            if b > r:
                t = b + d
            else:
                t = r + d
            idx = bisect.bisect_left(tmp['G'], t)
            if idx < y and tmp['G'][idx] == t:
                ret -= 1
    for g in tmp['G']:
        for b in tmp['B']:
            d = abs(b - g)
            if b > g:
                t = b + d
            else:
                t = g + d
            idx = bisect.bisect_left(tmp['R'], t)
            if idx < x and tmp['R'][idx] == t:
                ret -= 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
