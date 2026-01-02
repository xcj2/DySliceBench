def examC():
    A, B, C, X, Y = LI()
    ans = 0
    if A+B<=C*2:
        ans = A*X + B*Y
    else:
        Z = min(X,Y)
        ans = min(A,C*2)*max(X-Z,0) + min(B,C*2)*max(Y-Z,0) + C*Z*2
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
