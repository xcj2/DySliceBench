import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
import heapq

sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD


def fact_and_inv(SIZE):
    inv = [0] * SIZE  # inv[j] = j^{-1} mod MOD
    fac = [0] * SIZE  # fac[j] = j! mod MOD
    finv = [0] * SIZE  # finv[j] = (j!)^{-1} mod MOD
    inv[1] = 1
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, SIZE):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return fac, finv

def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret

def warshall_floyd(d, n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

class TwoDimGrid:
    # 2次元座標 -> 1次元
    def __init__(self, h, w, wall="#"):
        self.h = h
        self.w = w
        self.size = (h+2) * (w+2)
        self.wall = wall
        self.get_grid()

    def get_grid(self):
        grid = [self.wall * (self.w + 2)]
        for i in range(self.h):
            grid.append(self.wall + getS() + self.wall)

        grid.append(self.wall * (self.w + 2))
        self.grid = grid

    def pos(self, x, y):
        return y * (self.w + 2) + x + 1

    def search(self):
        grid = self.grid
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move_eight = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        ans = 0
        for i in range(1, self.h + 1):
            for j in range(1, self.w + 1):
                # pass # ここから何か書いてね
                cx, cy = j, i
                if grid[cy][cx] == ".":
                    ret = self.search_each(cx, cy)
                    ans = max(ans, ret)
        print(ans)

    def search_each(self, x, y):
        grid = self.grid
        d = deque()
        d.append((x,y))
        dist = [INF for i in range(self.size)]
        # print(x,y, self.size, self.pos(x,y))
        dist[self.pos(x,y)] = 0
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ret = 0
        while d:
            cx, cy = d.pop()
            ccos = dist[self.pos(cx, cy)]
            ret = max(ret, ccos)
            for mv in move:
                dx, dy = mv
                nx, ny = cx + dx, cy + dy
                # print(nx, ny)
                if grid[ny][nx] == ".":
                    if dist[self.pos(nx, ny)] > ccos + 1:
                        dist[self.pos(nx, ny)] = ccos + 1
                        d.append((nx, ny))

        return max([r for r in dist if r != INF])


def solve():
    h, w = getList()
    G = TwoDimGrid(h, w)
    G.search()
    return



def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()