#!/usr/bin/env python3
import sys
from collections import deque
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7

def array(*args, initial=0):
    pre = "[" * len(args)
    post = ""
    for a in args[::-1]:
        post += " for _ in range(" + str(a) + ")]"
    S = pre + "{}".format(initial) + post
    return eval(S)


def main():
    H, W, K = MAP()
    x1, y1, x2, y2 = MAP()
    # 空間はINF,壁は-1, →↑←↓
    pond = array(H + 2, W + 2, 4, initial=-1)
    for h in range(1, H + 1):
        for w, c in enumerate(input(), start=1):
            if c == ".":
                for i in range(4):
                    pond[h][w][i] = INF
    # 距離(), x, y, 方向
    q = deque()
    q.append(((0, 0), x1, y1, 0))
    q.append(((0, 0), x1, y1, 1))
    q.append(((0, 0), x1, y1, 2))
    q.append(((0, 0), x1, y1, 3))
    DX = (1, 0, -1, 0)
    DY = (0, 1, 0, -1)
    while q:
        new_q = deque()
        while q:
            (a0, a1), x, y, d = q.popleft()
            # 順方向へ進む
            nx = x + DX[d]
            ny = y + DY[d]
            # print((a0, a1), x, y, d, nx, ny)
            if pond[nx][ny][0] == -1:     # 行き止まりなら何もせず
                continue
            if pond[nx][ny][(d + 1) % 4] > a0 + 1:
                pond[nx][ny][(d + 1) % 4] = a0 + 1
                new_q.append(((a0 + 1, 0), nx, ny, (d + 1) % 4))
            if pond[nx][ny][(d - 1) % 4] > a0 + 1:
                pond[nx][ny][(d - 1) % 4] = a0 + 1
                new_q.append(((a0 + 1, 0), nx, ny, (d - 1) % 4))
            if pond[nx][ny][d] >= a0 + 1:
                pond[nx][ny][d] = a0 + 1
                if a1 + 1 < K:
                    q.append(((a0, a1 + 1), nx, ny, d))
                else:
                    new_q.append(((a0 + 1, 0), nx, ny, d))
            if (nx, ny) == (x2, y2):
                print(a0 + 1)
                return
        q = new_q
    print(-1)
    return


if __name__ == '__main__':
    main()
