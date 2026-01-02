#!/usr/bin/env python3
from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def LI(): return map(int, input().split())
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("INF")

#solve
def solve():
    h, w, K = LI()
    y1, x1, y2, x2 = LI()
    q = deque()
    field = [[False] * (w + 2)] + [None] * h + [[False] * (w + 2)]
    for i in range(1, h + 1):
        field[i] = [False] + [True] * w + [False]
    for i in range(1, h + 1):
        s = input().rstrip()
        for j in range(1, w + 1):
            if s[j-1] == "@":
                field[i][j] = False
    q.append((x1, y1))
    ans = 0
    c = [[0] * (w + 2) for i in range(h + 2)]
    while q:
        next_q = deque()
        while q:
            x, y = q.pop()
            if (x, y) == (x2, y2):
                print(ans)
                return
            for i in range(1, K + 1):
                if field[y + i][x]:
                    if not c[y + i][x]:
                        next_q.append((x, y + i))
                        c[y + i][x] = 1
                else:
                    break
            for i in range(1, K + 1):
                if field[y][x + i]:
                    if not c[y][x + i]:
                        next_q.append((x + i, y))
                        c[y][x + i] = 1
                else:
                    break
            for i in range(1, K + 1):
                if field[y - i][x]:
                    if not c[y - i][x]:
                        next_q.append((x, y - i))
                        c[y - i][x] = 1
                else:
                    break
            for i in range(1, K + 1):
                if field[y][x - i]:
                    if not c[y][x - i]:
                        next_q.append((x - i, y))
                        c[y][x - i] = 1
                else:
                    break
            field[y][x] = False
        ans += 1
        q = next_q
    print(-1)
    return


#main
if __name__ == '__main__':
    solve()
