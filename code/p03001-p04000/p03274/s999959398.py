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
    N, K = LI()
    X = LI()
    X = sorted(X)
    pos_q, neg_q = [], []
    cur_i = N - 1
    for x in X:
        if x < 0:
            neg_q.append(x)
        elif x == 0:
            K -= 1
        else:
            pos_q.append(x)
    if K == 0:
        print(0)
        return
    ans = inf
    pos_q = sorted(pos_q)
    neg_q = sorted(neg_q)[::-1]
    
    for ix, p in enumerate(pos_q):
        if K - ix - 1 > 0: # if still remains
            nokori = K - ix - 1
            if 0 <= nokori - 1 < len(neg_q):
                ans = min(abs(neg_q[nokori-1] - p - p), ans)
        else:
            ans = min(p, ans)

    for ix, n in enumerate(neg_q):
        if K - ix - 1 > 0:
            nokori = K - ix -1
            if 0 <= nokori - 1 < len(pos_q):
                ans = min(pos_q[nokori-1] + abs(n) + abs(n), ans)
        else:
            ans = min(abs(n), ans)
    print(ans)

main()

