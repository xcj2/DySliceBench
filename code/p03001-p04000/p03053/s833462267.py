import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

class TwoDimGrid:
    # 2次元座標 -> 1次元
    def __init__(self, h, w, wall="o"):
        self.h = h
        self.w = w
        self.size = (h+2) * (w+2)
        self.wall = wall
        self.get_grid()
        self.init_cost()

    def get_grid(self):
        grid = [self.wall * (self.w + 2)]
        for i in range(self.h):
            grid.append(self.wall + getS() + self.wall)

        grid.append(self.wall * (self.w + 2))
        self.grid = grid
    def init_cost(self):
        self.cost = [INF] * self.size

    def pos(self, x, y):
        # 壁も含めて0-indexed 元々の座標だけ考えると1-indexed
        return y * (self.w + 2) + x
    def getgrid(self, x, y):
        return self.grid[y][x]
    def get(self, x, y):
        return self.cost[self.pos(x, y)]
    def set(self, x, y, v):
        self.cost[self.pos(x, y)] = v
        return
    def show(self):
        for i in range(self.h+2):
            print(self.cost[(self.w + 2) * i:(self.w + 2) * (i+1)])
    def showsome(self, tgt):
        for t in tgt:
            print(t)
        return
    def showsomejoin(self, tgt):
        for t in tgt:
            print("".join(t))
        return

    def search(self):
        grid = self.grid
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        d = deque()
        for i in range(1, self.h+1):
            for j in range(1, self.w+1):
                if self.getgrid(j, i) == "#":
                    self.set(j, i, 0)
                    d.append((j, i, 0))
        # print(d)
        ans = 0
        while d:
            # print(d)
            cx, cy, cc = d.popleft()
            for dx, dy in move:
                nx, ny = dx + cx, dy + cy
                # print(nx, ny)
                if self.getgrid(nx, ny) == ".":

                    if self.get(nx, ny) > cc + 1:
                        ans = max(ans, cc + 1)
                        self.set(nx, ny, cc + 1)
                        d.append((nx, ny, cc + 1))

        # print(self.getgrid(1, 4))
        print(ans)



def solve():
    h, w = getList()
    g = TwoDimGrid(h, w)
    g.search()
def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





