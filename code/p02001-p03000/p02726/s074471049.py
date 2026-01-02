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
     
def main():
    N, X, Y = LI()
    X-=1
    Y-=1
    G = [[N+1 for _ in range(N)] for __ in range(N)]
    dists = []
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            # i->X->Y->j
            # i->j
            route = abs(X-i) + 1 + abs(Y-j)
            G[i][j] = min(abs(i-j), route)
            dists.append(G[i][j])
    c_dists = collections.Counter(dists)
    for i in range(1, N):
        print(c_dists[i])

main()

