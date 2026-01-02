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

def count_inside(x1, x2, y1, y2, points):
    cnt = 0
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    for p in points:
        if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            cnt += 1
    return cnt

def main():
    N, K = LI()
    points = []
    for _ in range(N):
        x, y = LI()
        points.append((x, y))
    points = sorted(points, key=lambda x: (x[0], x[1]))
    X = [p[0] for p in points]
    Y = [p[1] for p in points]
    area = inf
    for i in range(N):
        x1 = X[i]
        for j in range(i+1, N):
            x2 = X[j]
            for k in range(N):
                y1 = Y[k]
                for l in range(k+1, N):
                    y2 = Y[l]
                    if K == count_inside(x1, x2, y1, y2, points):
                        _area = abs(x1-x2) * abs(y1-y2)
                        area = min(_area, area)
    print(area)

main()

