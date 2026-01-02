# coding:utf-8

import sys
from collections import deque

INF = float('inf')
MOD = 10 ** 9 + 7
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    h, w = LI()
    B = [list(SI()) for _ in range(h)]

    D = deque()
    for i, row in enumerate(B):
        for j, c in enumerate(row):
            if c == '#':
                D.append((i, j, 0))

    while D:
        y, x, cnt = D.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0 <= yy < h and 0 <= xx < w:
                if B[yy][xx] == '#':
                    continue
                B[yy][xx] = '#'
                D.append((yy, xx, cnt + 1))

    print(cnt)




if __name__ == '__main__':
    main()
