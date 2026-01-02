
def examC():
    N = I()
    S = SI()
    cumE = [0]*(N+1)
    for i in range(N):
        cur = 0
        if S[i]=="E":
            cur = 1
        cumE[i+1] = cumE[i] + cur
    ans = N-1
    for i in range(1,N+1):
        cur = (i-1-cumE[i-1]) + (cumE[N]-cumE[i])
        ans = min(ans,cur)
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
