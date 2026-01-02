#!/usr/bin/env python3
import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]

def main():
    H, W, K = MAP()
    HH = max(H, W) + 2
    x1, y1, x2, y2 = LIST()
    c = [[-1] + [0 if c == "." else -1 for c in input()] + [-1]
         for i in range(H)]
    c = [[-1] * (W + 2)] + c + [[-1] * (W + 2)]

    # 0123: 上下左右
    stack = deque([(x1, y1, 0), (x1, y1, 1),
                   (x1, y1, 2), (x1, y1, 3)])
    append, popleft = stack.append, stack.popleft
    DX = (1, 0, -1, 0)
    DY = (0, 1, 0, -1)
    while stack:
        x, y, d = popleft()
        flag = True
        a = c[x][y] + 1
        for k in range(1, K + 1):
            xx, yy = x + k * DX[d], y + k * DY[d]
            if c[xx][yy] == 0:
                b = c[xx + DX[(d - 1) % 4]][yy + DY[(d - 1) % 4]]
                if b == 0 or b == a + 1:
                    append((xx, yy, (d - 1) % 4))
                b = c[xx + DX[(d + 1) % 4]][yy + DY[(d + 1) % 4]]
                if b == 0 or b == a + 1:
                    append((xx, yy, (d + 1) % 4))
                c[xx][yy] = a
            elif c[xx][yy] != a:
                flag = False
                break
        if flag:
            append((xx, yy, d))
        if c[x2][y2] > 0:
            print(c[x2][y2])
            return

    print(-1)
    return


if __name__ == '__main__':
    main()
