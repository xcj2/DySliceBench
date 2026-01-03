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
    N, M = LI()
    d = [inf for _ in range(N)]
    d[0] = 0
    edges = []
    for _ in range(M):
        a, b, c = LI_()
        c += 1
        edges.append((a, b, -c))
    for _ in range(N-1):
        for edge in edges:
            fr, to, cost = edge
            if d[to] > d[fr] + cost:
                d[to] = d[fr] + cost
    neg = [False for _ in range(N)]
    for _ in range(N):
        for edge in edges:
            fr, to, cost = edge
            if neg[fr] == True:
                neg[to] = True
            if d[to] > d[fr] + cost:
                neg[to] = True
    if neg[N-1]:
        print('inf')
    else:
        print(-d[N-1])

main()

