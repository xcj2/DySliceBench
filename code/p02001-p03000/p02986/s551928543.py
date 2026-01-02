import sys
input=sys.stdin.readline
from collections import deque
class LCA:
    def __init__(self,v,Edges,root=0):
        self.v=v
        self.Edges=Edges
        self.maxLog=18
        self.Parent=[[-1]*v for _ in range(self.maxLog+1)]
        self.Depth=[0]*v
        self.__bfs(root)
        for i in range(self.maxLog):
            for j in range(v):
                if self.Parent[i][j]!=-1:
                    self.Parent[i+1][j]=self.Parent[i][self.Parent[i][j]]
    def __bfs(self,root):
        Visited=[False]*self.v
        Visited[root]=True
        q=deque([root])
        while q:
            fr=q.pop()
            for to in self.Edges[fr]:
                if Visited[to]:
                    continue
                self.Parent[0][to]=fr
                self.Depth[to]=self.Depth[fr]+1
                Visited[to]=True
                q.append(to)
    def lca(self,a,b):
        if self.Depth[a]>self.Depth[b]:
            a,b=b,a
        for i in range(self.maxLog):
            if (self.Depth[b]-self.Depth[a])&(1<<i):
                b=self.Parent[i][b]
        if a==b:
            return b
        for i in reversed(range(self.maxLog-1)):
            if self.Parent[i][a]!=self.Parent[i][b]:
                a=self.Parent[i][a]
                b=self.Parent[i][b]
        return self.Parent[0][a]

def Eulertour(Edges,n,root=0):
    Euler=[]
    Depth=[-1]*n
    Depth[root]=0
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
                que2.append(to)
        que.extend(que2)
        que2=deque()
        Visited[fr]=True
    return Euler

n,q=map(int,input().split())
Edgedict=[dict() for _ in range(n)]
for _ in range(n-1):
    a,b,c,d=map(int,input().split())
    a-=1; b-=1
    Edgedict[a][b]=(c,d)
    Edgedict[b][a]=(c,d)
Queries=[tuple(map(int,input().split())) for _ in range(q)]
Euler=Eulertour(Edgedict,n)
lca=LCA(n,Edgedict)
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