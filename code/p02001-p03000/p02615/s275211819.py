#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
import heapq
def resolve():
    N,=pin()
    A=[*pin()]
    A.sort(reverse=True)

    ans=0
    h=[]
    heapq.heappush(h,0)
    for i in range(1,N):
        temp=heapq.heappop(h)
    #    print(temp)
        ans+=A[temp]
        heapq.heappush(h,i)
        heapq.heappush(h,i)
    print(ans)

#%%submit!
resolve()