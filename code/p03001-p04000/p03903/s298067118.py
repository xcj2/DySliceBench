import sys
input = sys.stdin.readline
from operator import itemgetter
from collections import deque

class Unionfindtree:
    def __init__(self, number):
        self.par = [i for i in range(number)]
        self.rank = [0] * (number)

    def find(self, x):  # 親を探す
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):  # x,yを繋げる
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        else:
            self.par[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

    def connect(self, x, y):  # 親が同じかみる
        return self.find(x) == self.find(y)


N,M=map(int,input().split())
table=[[int(i) for i in input().split()]for i in range(M)]
Q=int(input())
query=[[int(i) for i in input().split()]for i in range(Q)]
table = sorted(table,key=itemgetter(2))
if N<3:
    for a,b in query:
        print(0)
    sys.exit()
T=Unionfindtree(N)
sear=Unionfindtree(2*N-1)
ans=0
value=[0]*(N+N-1)
dp=[[0]*(2*N-1) for i in range(16)]
table2=[[] for i in range(2*N-1)]
s=0
for i in range(M):
    a,b,c=table[i]
    a,b=a-1,b-1
    if not T.connect(a,b):
        ans+=c
        T.union(a,b)
        value[s+N]=c
        le=a
        ri=b
        for j in range(s+N,N-1,-1):
            if sear.connect(a,j):
                le=j
                break
        for j in range(s+N,N-1,-1):
            if sear.connect(b,j):
                ri=j
                break
        table2[s+N].append(le)
        table2[s+N].append(ri)
        sear.union(le,s+N)
        sear.union(ri,s+N)
        s+=1
    if s==N-1:
        break

H=deque()
H.append((0,2*N-2))
depth=[-1]*(2*N-1)
depth[2*N-2]=0
while H:
    dep,pt=H.popleft()
    for p in table2[pt]:
        H.append((dep+1,p))
        depth[p]=dep+1
        dp[0][p]=pt
#print(table2)
#print(depth,dp[0])

for k in range(1,16):
    for x in range(2*N-1):
        dp[k][x]=dp[k-1][dp[k-1][x]]
def LCA(s,t):
    if depth[s]>depth[t]:
        s,t=t,s
    for k in range(16):
        if ((depth[t]-depth[s] )>>k) & 1:
            t = dp[k][t]
    if s==t:
        return s
    for k in range(15,-1,-1):
        if dp[k][s]!=dp[k][t]:
            s=dp[k][s]
            t=dp[k][t]
    return dp[0][s]

for s,t in query:
    s,t=s-1,t-1
    pa=LCA(s,t)
    #print(pa,value[pa])
    print(ans-value[pa])



