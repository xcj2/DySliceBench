import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def count_inside(p1, p2, points):
    cnt = 0
    min_x = min(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_x = max(p1[0], p2[0])
    max_y = max(p1[1], p2[1])
    for p in points:
        if min_x <= p[0] <= max_x and min_y <= p[1] <= max_y:
            cnt += 1
    return cnt

def main():
    N, K = LI()
    points = []
    X, Y = [], []
    for i, _ in enumerate(range(N)):
        x, y = LI()
        points.append((x, y))
        X.append((x, i))
        Y.append((y, i))
    X = sorted(X, key=lambda x: x[0])
    Y = sorted(Y, key=lambda x: x[0])
    mapOrder2x = {}
    mapOrder2y = {}

    zaatsu_X = [-1 for _ in range(N)]
    zaatsu_Y = [-1 for _ in range(N)]

    for order, (x, i) in enumerate(X):
        zaatsu_X[i] = order
        mapOrder2x[order] = x

    for order, (y, i) in enumerate(Y):
        zaatsu_Y[i] = order
        mapOrder2y[order] = y

    assert(-1 not in zaatsu_X)
    assert(-1 not in zaatsu_Y)

    G = [[0 for _ in range(N)] for __ in range(N)]
    cumsum = [[0 for _ in range(N+1)] for __ in range(N+1)]

    for x, y in zip(zaatsu_X, zaatsu_Y):
        G[x][y] = 1

    for x in range(N):
        for y in range(N):
            cumsum[x+1][y+1] = cumsum[x+1][y] + cumsum[x][y+1] - cumsum[x][y] + G[x][y]

    def query_cumsum2d(s, r1, r2, c1, c2):
        if c2 < c1:
            c1, c2 = c2, c1
        if r2 < r1:
            r1, r2 = r2, r1
        return s[r2][c2] - s[r2][c1] - s[r1][c2] +s[r1][c1]

    def calc_area(x1, x2, y1, y2, mapx, mapy):
        return abs(mapx[x1] - mapx[x2]) * abs(mapy[y1] - mapy[y2])

    area = inf
    for r1 in range(0, N):
        for r2 in range(r1, N+1):
            for c1 in range(0, N):
                for c2 in range(c1, N+1):
                    if K == query_cumsum2d(cumsum, r1, r2, c1, c2):
                        
                        _area = calc_area(r1, r2-1, c1, c2-1, mapOrder2x, mapOrder2y)
                        area = min(area, _area)
    print(area)
main()

