def examB():
    X = S()
    sumS = 0
    for i in X:
        sumS += int(i)
    judge = int(X)%sumS
    if judge==0:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)

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
