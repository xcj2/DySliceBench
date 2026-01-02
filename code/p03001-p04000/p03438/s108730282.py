def examB():
    N = I()
    A = LI(); B = LI()
    dif = sum(B) -sum(A)
    cur = 0
    for i in range(N):
        if A[i]>=B[i]:
            cur += A[i]-B[i]
        elif (A[i]-B[i])%2==1:
            cur +=1
    if dif>=cur:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)

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
