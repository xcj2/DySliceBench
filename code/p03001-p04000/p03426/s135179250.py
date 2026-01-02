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
     
def diff(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():
    H, W, D = LI()
    A = []
    for _ in range(H):
        A.append(LI())
    Q = I()
    LR = []
    for _ in range(Q):
        LR.append(LI())
    nums = [[] for _ in range(90000)]
    valAndPoint = []
    for r in range(H):
        for c in range(W):
            valAndPoint.append((A[r][c], (r, c)))
    valAndPoint = sorted(valAndPoint, key=lambda x: x[0])
    dists = [[] for _ in range(90000)]
    for val, point in valAndPoint:
        nums[val % D].append(point) # val // D番目
    cum_nums = [[0] for _ in range(90000)]
    for amari, points in enumerate(nums):
        if len(points) < 1:
            continue
        cur_p = points[0]
        for p in points[1:]:
            dists[amari].append(diff(cur_p, p))
            ix = len(dists[amari])
            cum_nums[amari].append(cum_nums[amari][ix-1] + diff(cur_p, p))
            cur_p = p
    for lr in LR:
        l = lr[0]
        r = lr[1]
        l_amari = l % D

        st_hops = l // D
        en_hops = r // D
        if l % D == 0:
            st_hops -= 1
            en_hops -= 1
        print(cum_nums[l_amari][en_hops] - cum_nums[l_amari][st_hops])
main()

