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
    X = LI()
    X = sorted(X)
    diff = []
    for i in range(M-1):
        d = X[i+1] - X[i]
        diff.append(d)
    diff = sorted(diff)
    while N - 1> 0 and len(diff) > 0:
        diff.pop()
        N -= 1
    ans = sum(diff)
    print(ans)
    '''
    X = sorted(X)
    min_dist = [0] * M
    if N == 1:
        return X[-1] - X[0]
    print(X)
    for i in range(1, M-1):
        min_dist[i] = min(abs(X[i] - X[i-1]), abs(X[i+1] - X[i]))
        print(min_dist)
    min_dist = sorted(min_dist)[::-1]
    print(min_dist)
    for i in range(N-2):
        if len(min_dist) > 0:
            min_dist.pop(-1)
    print(sum(min_dist))
    '''
main()

