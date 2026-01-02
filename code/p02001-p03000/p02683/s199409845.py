import sys
import sys
from collections import Counter
from collections import deque
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,m,x=mp()
l=[lmp() for i in range(n)]
ans=[]
for i in range(2**n):
    b=bin(i)[2:]
    c=b.zfill(n)
    q=[0]*(m+1)
    for k in range(n):
        if c[k]=="0":
            for j in range(0,m+1):
                q[j]+=l[k][j]



    ch=0
    for j in range(1,m+1):
        if q[j]<x:
            ch=1
    if ch==0:
        ans.append(q[0])
if len(ans)==0:
    print(-1)
else:
    print(min(ans))