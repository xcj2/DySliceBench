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
    N, Q = LI()
    edge, P, X = [], [], []
    ans = [0 for _ in range(N)]
    for _ in range(N-1):
        _a, _b = LI()
        edge.append((_a-1, _b-1))
    edge = sorted(edge, key=lambda x:x[0])
    for _ in range(Q):
        _p, _x = LI()
        ans[_p-1] += _x
    for i in range(N-1):
        a_nodenum = edge[i][0]
        b_nodenum = edge[i][1]
        ans[b_nodenum] += ans[a_nodenum]
    for i in ans:
        print(i, end=" ")
    print()
main()

