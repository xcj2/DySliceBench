import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
class LCA:
    def __init__(self,V,edges,depth,parent,root=0):
        self.edges=edges
        self.maxLog=18
        self.parent=[[-1]*V for _ in range(self.maxLog+1)]
        self.parent[0]=parent
        self.depth=depth
        for i in range(self.maxLog):
            for j in range(V):
                if self.parent[i][j]!=-1:
                    self.parent[i+1][j]=self.parent[i][self.parent[i][j]]
    def lca(self,a,b):
        if self.depth[a]>self.depth[b]:
            a,b=b,a
        for i in range(self.maxLog):
            if (self.depth[b]-self.depth[a])&(1<<i):
                b=self.parent[i][b]
        if a==b:
            return b
        for i in reversed(range(self.maxLog-1)):
            if self.parent[i][a]!=self.parent[i][b]:
                a=self.parent[i][a]
                b=self.parent[i][b]
        return self.parent[0][a]

from collections import deque
def Eulertour(Edges,n,root=0):
    Euler=[]
    Depth=[-1]*n
    Depth[root]=0
    Parent=[-1]*n
    que=deque([root])
    que2=deque()
    Visited=[False]*n
    while que:
        fr=que.pop()
        Euler.append((Depth[fr],fr))
        if Visited[fr]:
            continue
        for to in Edges[fr]:
            if Visited[to]:
                que.append(to)
            else:
                Depth[to]=Depth[fr]+1
                Parent[to]=fr
                que2.append(to)
        que.extend(que2)
        que2=deque()
        Visited[fr]=True
    return Euler,Depth,Parent

n,q=map(int,input().split())
Edgedict=[dict() for _ in range(n)]
for _ in range(n-1):
    a,b,c,d=map(int,input().split())
    a-=1; b-=1
    Edgedict[a][b]=(c,d)
    Edgedict[b][a]=(c,d)
Queries=[tuple(map(int,input().split())) for _ in range(q)]
Euler,Depth,Parent=Eulertour(Edgedict,n)
lca=LCA(n,Edgedict,Depth,Parent)
Q=[[] for _ in range(n)]
for i,(x,y,u,v) in enumerate(Queries):
    u-=1; v-=1
    Q[u].append([i,x,y,True])
    Q[v].append([i,x,y,True])
    Q[lca.lca(u,v)].append([i,x,y,False])
Ans=[0]*q
dist=0
C_len=[0]*n
C_cnt=[0]*n
for i in range(1,len(Euler)):
    idx=Euler[i][1]
    c,l=Edgedict[Euler[i-1][1]][idx]
    if Euler[i-1][0]<Euler[i][0]:
        dist+=l
        C_len[c]+=l
        C_cnt[c]+=1
        for q_idx,x,y,flag in Q[idx]:
            if flag:
                Ans[q_idx]+=dist+C_cnt[x]*y-C_len[x]
            else:
                Ans[q_idx]-=(dist+C_cnt[x]*y-C_len[x])*2
    else:
        dist-=l
        C_len[c]-=l
        C_cnt[c]-=1
print(*Ans,sep='\n')