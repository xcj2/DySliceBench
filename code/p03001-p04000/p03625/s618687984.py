def examC():
    N = I()
    A = LI(); A.sort(reverse = True)
    d = defaultdict(int)
    cur = []
    ans = 0
    for i in range(N):
        d[A[i]] +=1
        if d[A[i]]==2:
            cur.append(A[i])
        elif d[A[i]]==4:
            cur.append(A[i])
        if len(cur)==2:
            ans = cur[0] * cur[1]
            break
    print(ans)


import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
