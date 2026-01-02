import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
n,k=NM()
l=LL(n)
l.sort(key=lambda x:-x[1])
from heapq import heappush,heappop,heapify
s=set()
q=[]
oisisa=0
syu=0
for t,d in l[:k]:
    if t in s:
        heappush(q,d)
    else:
        s.add(t)
        syu+=1
    oisisa+=d
ans=oisisa+syu**2
for t,d in l[k:]:
    if q and not t in s:
        syu+=1
        oisisa+=d-heappop(q)
        s.add(t)
    ans=max(ans,oisisa+syu**2)
print(ans)