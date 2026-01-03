"""
最小共通祖先(LCA, lowest common ancestor)を求める
"""
class LCA_doubling:
    """
    parent: ダブリングテーブル
    depth: 元の深さ
    """
    def __init__(self,g,root): #g: graph 
        def dfs(v,p): #p: parent of v
            if p != -1: self.depth[v] = self.depth[p]+1
            for c,d in g[v]:
                if c == p: continue
                self.parent[0][c] = v
                self.dist[0][c] = d
                dfs(c,v)

        def doubling_make_table(N,logN,Table,Dist):
            for i in range(1,logN):
                for j, Tiij in enumerate(Table[i-1]):
                    if Tiij != -1:
                        Table[i][j] = Table[i-1][Tiij]
                        Dist[i][j] = Dist[i-1][j] + Dist[i-1][Tiij]

        N = len(g)
        self.logN = len(bin(N))-2
        self.parent = [[-1]*N for _ in range(self.logN)]
        self.dist   = [[0]*N for _ in range(self.logN)]
        self.depth = [0]*(N) #ノードの深さ
        dfs(root,-1) #root を根とする木と見て計算
        doubling_make_table(N, self.logN, self.parent, self.dist) #ダブリングのテープル構築


    def getLCA(self,u,v): #u,vのdistを返す
        if self.depth[u] > self.depth[v]: u,v = v,u #vが深い
        d = 0
        dd = self.depth[v] - self.depth[u]
        for k in range(self.logN-1,-1,-1):
            if (dd >> k) & 1:
                d += self.dist[k][v]
                v = self.parent[k][v]
        if u == v: return u, d;
        for k in range(self.logN-1,-1,-1):
            if self.parent[k][u] != self.parent[k][v]:
                d += self.dist[k][u]
                d += self.dist[k][v]
                u,v = self.parent[k][u], self.parent[k][v]
        return self.parent[0][u], d+self.dist[0][u]+self.dist[0][v];

    def getdepth(self,u): #uの深さを返す
        return self.depth[u]



import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a,b,c = [int(i) for i in readline().split()]
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))

LCA = LCA_doubling(g, root=0)
#print(LCA.parent)
#print(LCA.depth)
#print(LCA.dist)

"""
ABC070D

"""
q,k = [int(i) for i in readline().split()]
k -= 1
for _ in range(q):
    a,b = [int(i)-1 for i in readline().split()]
    
    u1,d1 = LCA.getLCA(a,k)
    u2,d2 = LCA.getLCA(b,k)
    print(d1+d2)



