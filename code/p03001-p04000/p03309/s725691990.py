
def examC():
    N = I()
    A = LI()
    newA = []
    for i in range(N):
        cur = A[i]-i-1
        newA.append(cur)
    newA.sort()
    b = newA[N//2]
    ans = 0
    for i in range(N):
        ans += abs(newA[i]-b)
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

examC()
