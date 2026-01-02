#!/usr/bin/env python3
import sys
from heapq import heappush, heappop, heapify
from math import ceil
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7
EPS = 1e-6


def main():
    H, W, K = MAP()
    x1, y1, x2, y2 = LIST()
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    c = [[c for c in input()] for i in range(H)]
    dist = [[INF] * W for i in range(H)]
    dist[x1][y1] = 0

    # 0123: 上下左右
    stack = [(0, x1, y1, 0), (0, x1, y1, 1),
             (0, x1, y1, 2), (0, x1, y1, 3)]
    head = 0
    while head < len(stack):
        curr, x, y, d = stack[head]
        head += 1
        c[x][y] = "@"
        # print(curr, x, y, d, head)
        # print(stack)
        if d == 0:
            dx, dy = 1, 0
        elif d == 1:
            dx, dy = 0, 1
        elif d == 2:
            dx, dy = -1, 0
        else:
            dx, dy = 0, -1
        flag = True
        for i in range(1, K + 1):
            xx = x + i * dx
            yy = y + i * dy
            if not(0 <= xx < H) or not(0 <= yy < W) or c[xx][yy] == "@":
                flag = False
                break
            if (xx, yy) == (x2, y2):
                print(int(ceil(curr + 1 / K - EPS)))
                return
            if dist[xx][yy] > curr + 1:
                dist[xx][yy] = curr + 1
                stack.append((curr + 1, xx, yy, (d - 1) % 4))
                stack.append((curr + 1, xx, yy, (d + 1) % 4))
        if flag:
            if dist[xx][yy] >= curr + 1:
                stack.append((curr + 1, xx, yy, d))
    print(-1)
    return


if __name__ == '__main__':
    main()
