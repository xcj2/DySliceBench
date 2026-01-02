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
    def dist(self,a,b):
        lca=self.lca(a,b)
        return self.Depth[a]+self.Depth[b]-2*self.Depth[lca]

def main():
    n,u,v=map(int,input().split())
    u-=1; v-=1
    Edges=[[] for _ in range(n)]
    for _ in range(n-1):
        x,y=map(lambda i: int(i)-1,input().split())
        Edges[x].append(y)
        Edges[y].append(x)
    L=[]
    for i in range(n):
        if len(Edges[i])==1:
            L.append(i)
    lca=LCA(n,Edges,v)
    dist=lca.dist(u,v)
    ans=dist//2
    for l in L:
        m=lca.lca(u,l)
        if lca.dist(u,m)>=lca.dist(v,m):
            continue
        d_u=lca.dist(u,l)
        d_v=lca.dist(v,l)
        d=d_v-d_u
        cnt=d-1
        ans=max(ans,d_u+cnt)
    print(ans)
    
if __name__=='__main__':
    main()