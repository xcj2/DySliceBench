def examD():
    N = I()
    g, s, c = [0]*2, [0]*2, [0]*2
    for i in range(2):
        g[i],s[i],c[i] = LI()
    dp1 = [0]*(N+1)
    v1 = [g[1]-g[0],s[1]-s[0],c[1]-c[0]]
    w1 = [g[0],s[0],c[0]]
    v2 = [g[0]-g[1],s[0]-s[1],c[0]-c[1]]
    w2 = [g[1],s[1],c[1]]
    for i in range(N):
        if i+w1[0]<=N:
            dp1[i+w1[0]] = max(dp1[i+w1[0]],dp1[i]+v1[0])
        if i+w1[1]<=N:
            dp1[i+w1[1]] = max(dp1[i+w1[1]],dp1[i]+v1[1])
        if i+w1[2]<=N:
            dp1[i+w1[2]] = max(dp1[i+w1[2]],dp1[i]+v1[2])
    newN = max(dp1)+N
#    print(newN)
    dp2 = [0]*(newN+1)
    for i in range(newN):
        if v2[0]>0 and i+w2[0]<=newN:
            dp2[i+w2[0]] = max(dp2[i+w2[0]],dp2[i]+v2[0])
        if v2[1]>0 and i+w2[1]<=newN:
            dp2[i+w2[1]] = max(dp2[i+w2[1]],dp2[i]+v2[1])
        if v2[2]>0 and i+w2[2]<=newN:
            dp2[i+w2[2]] = max(dp2[i+w2[2]],dp2[i]+v2[2])
    ans = dp2[newN]+newN
    print(ans)

from string import digits
import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()