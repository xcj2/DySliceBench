#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from collections import deque
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7
EPS = 1e-6
KETA = 10**7


def main():
    H, W, K = MAP()
    x1, y1, x2, y2 = LIST()
    c = [[-1] + [0 if c == "." else -1 for c in input()] + [-1]
         for i in range(H)]
    c = [[-1] * (W + 2)] + c + [[-1] * (W + 2)]
    c[x1][y1] = 0

    # 0123: 上下左右
    stack = deque([((x1 * KETA + y1) << 2) + 0, ((x1 * KETA + y1) << 2) + 1,
                   ((x1 * KETA + y1) << 2) + 2, ((x1 * KETA + y1) << 2) + 3])
    DX = (1, 0, -1, 0)
    DY = (0, 1, 0, -1)
    head = 0
    while stack:
        b = stack.popleft()
        head += 1
        d = b % 4
        x, y = divmod(b >> 2, KETA)
        flag = True
        a = c[x][y] + 1
        for k in range(1, K + 1):
            xx, yy = x + k * DX[d], y + k * DY[d]
            if c[xx][yy] == 0:
                stack.append(((xx * KETA + yy) << 2) + (d - 1) % 4)
                stack.append(((xx * KETA + yy) << 2) + (d + 1) % 4)
                c[xx][yy] = a
            elif c[xx][yy] != a:
                flag = False
                break
        if flag:
            stack.append(((xx * KETA + yy) << 2) + d)
        if c[x2][y2] > 0:
            print(c[x2][y2])
            return

    print(-1)
    return


if __name__ == '__main__':
    main()
