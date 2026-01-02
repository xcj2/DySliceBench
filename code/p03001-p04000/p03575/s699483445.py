import sys
from collections import Counter
from collections import deque
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,m=mp()
edge=[lmp() for i in range(m)]
ans=0
for _ in range(m):
    l=[[] for i in range(n+1)]
    que=deque()
    ch=[0]*(n+1)
    ch[0]=1
    for i in range(m):
        if i!=_:
            l[edge[i][0]].append(edge[i][1])
            l[edge[i][1]].append(edge[i][0])
    q=1
    que.append(l[q])
    ch[1]=1
    while len(que):
        q=que.pop()
        for j in range(len(q)):
            if ch[q[j]]==0:
                que.append(l[q[j]])
                ch[q[j]]=1
    b=0
    for k in range(n+1):
        if ch[k]==0:
            b=1
    if b==1:
        ans+=1
print(ans)