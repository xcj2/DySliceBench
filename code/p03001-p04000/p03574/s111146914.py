def examB():
    H, W = LI()
    St = [S() for _ in range(H)]
    ans = [[] for _ in range(H)]
    for i1,l in enumerate(St):
        for i2,j in enumerate(l):
            cur = int(0)
            if j==".":
                for k in range(3):
                    for p in range(3):
                        if 0<=i1-1+k<H and 0<=i2-1+p<W:
                            if St[i1 - 1 + k][i2 - 1 + p] == "#":
                                cur += 1
            else:
                cur = "#"
            ans[i1].append(str(cur))
    for v in ans:
        print("".join(map(str,v)))



import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
