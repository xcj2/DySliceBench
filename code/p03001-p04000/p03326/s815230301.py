#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, x: "List[int]", y: "List[int]", z: "List[int]"):
    ret = -float('inf')
    for b in range(8):
        c = [1] * 3
        for k in range(3):
            if (1 << k) & b:
                c[k] = -1
        s = []
        for i in range(N):
            s.append(x[i] * c[0] + y[i] * c[1] + z[i] * c[2])
        s.sort(reverse=True)
        ret = max(ret, sum(s[:M]))
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    z = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        z[i] = int(next(tokens))
    solve(N, M, x, y, z)

if __name__ == '__main__':
    main()
