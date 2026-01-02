def examB():
    A, B, K = LI()
    ans = []
    for i in range(K):
        low = min(B,A+i); up = max(B-i,A)
        if low not in ans:
            ans.append(low)
        if up not in ans:
            ans.append(up)
    ans.sort()
    for v in ans:
        print(v)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
