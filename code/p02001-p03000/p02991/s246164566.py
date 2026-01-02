def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]
e=[[] for i in range(3*10**5+10)]

[n,m]=i2()
for i in range(m):
 [u,v]=i2()
 u-=1
 v-=1
 e[3*u].append(3*v+1)
 e[3*u+1].append(3*v+2)
 e[3*u+2].append(3*v)
 
[s,t]=i2()
s-=1
t-=1
from collections import deque
d=[-1 for i in range(3*10**5+10)]
def bfs(v):
   d[v]=0
   q=deque([v])
   while len(q):
    v=q.popleft()
    for i in e[v]:
      if d[i]<0:
         d[i]=d[v]+1
         q.append(i)
   if d[3*t]>-1:
     return d[3*t]//3
   return d[3*t]  
print(bfs(3*s))