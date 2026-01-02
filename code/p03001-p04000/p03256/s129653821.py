def examC():
    N,M = LI()
    S = SI()
    V = [[] for _ in range(N)]
    ok = [1]*N
    acnt = [0]*N; bcnt = [0]*N
    for _ in range(M):
        a, b = LI()
        V[a-1].append(b-1)
        V[b-1].append(a-1)
        if S[a-1]=="A":
            acnt[b-1] +=1
        else:
            bcnt[b-1] +=1
        if S[b-1]=="A":
            acnt[a-1] +=1
        else:
            bcnt[a-1] +=1
    NGque = deque()
    for i in range(N):
        if acnt[i]==0 or bcnt[i]==0:
            ok[i]=0
            NGque.append(i)
#    print(ok,acnt,bcnt)
#    print(NGque)
    while(NGque):
        cur = NGque.pop()
        for i in V[cur]:
            if ok[i]==1:
                if S[cur] == "A":
                    acnt[i] -= 1
                else:
                    bcnt[i] -= 1
                if acnt[i] == 0 or bcnt[i] == 0:
                    ok[i] = 0
                    NGque.append(i)
    if max(ok)==1:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
