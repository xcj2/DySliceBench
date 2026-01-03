#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(W: int, H: int, N: int, a: "List[int]", b: "List[int]"):
    ret = [0] * 10
    ret[0] = (H - 2) * (W - 2)
    reduces = []
    for i in range(N):
        lx = max(0, a[i] - 3)
        rx = min(W - 2, a[i])
        ly = max(0, b[i] - 3)
        ry = min(H - 2, b[i])
        for bx in range(lx, rx):
            for by in range(ly, ry):
                reduces.append((bx, by))
    reduces.sort()
    cnt = 1
    for i in range(1, len(reduces)):
        if reduces[i] == reduces[i - 1]:
            cnt += 1
        else:
            ret[0] -= 1
            ret[cnt] += 1
            cnt = 1
    if len(reduces):
        ret[0] -= 1
        ret[cnt] += 1
    for r in ret:
        print(r)
    return


def _solve(W: int, H: int, N: int, a: "List[int]", b: "List[int]"):
    ret = [0] * 10
    ret[0] = (H - 2) * (W - 2)
    reduces = []
    for i in range(N):
        lx = max(0, a[i] - 3)
        rx = min(W - 2, a[i])
        ly = max(0, b[i] - 3)
        ry = min(H - 2, b[i])
        for bx in range(lx, rx):
            for by in range(ly, ry):
                cnt = 0
                for x in range(0, 3):
                    for y in range(0, 3):
                        #print(a[i] - 1, b[i] - 1, bx + x, by + y)
                        if grid[by + y][bx + x]:
                            cnt += 1
                ret[cnt] -= 1
                ret[cnt + 1] += 1
        #print(b[i] - 1, a[i] - 1, H, W)
        grid[b[i] - 1][a[i] - 1] = True
    for r in ret:
        print(r)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]" 
    b = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(H, W, N, a, b)

if __name__ == '__main__':
    main()
