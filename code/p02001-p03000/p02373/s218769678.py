import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

class LCA():

    def __init__(self,G,root = 0): #O(NlogN)
        self.n = len(G)
        self.G = G
        self.root = root
        self.K = 1 #2 ** K > nとなる最小のK
        while (1<<self.K) <= self.n:
            self.K += 1
        self.parents = [[-1] * self.n for _ in range(self.K)]
        self.dist = [0] * self.n
        
        self._dfs(root,0,-1)
        for k in range(self.K - 1):
            for v in range(self.n):
                if self.parents[k][v] >= 0:
                    self.parents[k + 1][v] = self.parents[k][self.parents[k][v]]
    
    def _dfs(self,i,d,p):
        self.parents[0][i] = p
        self.dist[i] = d
        for e in self.G[i]:
            if e != p:
                self._dfs(e,d + 1,i)
    
    def qry(self,u,v): #O(logN)
        if self.dist[u] < self.dist[v]:
            u,v = v,u
        
        dif = self.dist[u] - self.dist[v]
        for k in range(self.K):
            if dif >> k & 1:
                u = self.parents[k][u]
        
        if u == v:
            return u
        
        for k in range(self.K - 1,-1,-1):
            if self.parents[k][u] != self.parents[k][v]:
                u = self.parents[k][u]
                v = self.parents[k][v]
        
        return self.parents[0][u]

def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for i in range(n):
        a = list(map(int,input().split()))
        k = a[0]
        for e in a[1:]:
            G[e].append(i)
            G[i].append(e)

    lca = LCA(G)
    q = int(input())
    for _ in range(q):
        u,v = map(int,input().split())
        print(lca.qry(u,v))

if __name__ == '__main__':
    main()

