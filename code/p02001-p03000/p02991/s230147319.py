import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    n,m = inpm()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u,v = inpm()
        u -= 1
        v -= 1
        g[u].append(v)
    s,t = inpm()
    s -= 1
    t -= 1
    que = deque()
    que.append(s)
    visited1 = [0 for _ in range(n)]
    visited2 = [0 for _ in range(n)]
    visited3 = [0 for _ in range(n)]
    visited3[s] = 1
    cnt = 1
    while True:
        tank1 = deque()
        tank2 = deque()
        tank3 = deque()
        while que:
            start = que.pop()
            for go in g[start]:
                if not visited1[go]:
                    visited1[go] = 1
                    tank1.append(go)
        while tank1:
            start = tank1.pop()
            for go in g[start]:
                if not visited2[go]:
                    visited2[go] = 1
                    tank2.append(go)
        while tank2:
            start = tank2.pop()
            for go in g[start]:
                if not visited3[go]:
                    visited3[go] = 1
                    tank3.append(go)
                if go == t:
                    print(cnt)
                    return
        que = tank3
        cnt += 1
        if que == deque():
            break
    print(-1)
    
if __name__ == "__main__":
    main()