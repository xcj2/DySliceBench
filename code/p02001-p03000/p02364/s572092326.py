class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ
 
    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]
 
    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
 
    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)
 
    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]

def kruskal(max_vertex,edges):
    edges.sort(key=lambda x:x[2])#costでソート
    uf=UnionFind(max_vertex)
    mst=[]
    for edge_cost in edges:
        es,ee,cost=edge_cost
        if not uf.is_same(es,ee):
            uf.unite(es,ee)
            mst.append([(es,ee),cost])
    return mst
         


#costでソートするから[頂点,頂点,重み]でもったほうがいいのでは
v,e=map(int,input().split())#v: 頂点の数 e:辺の数
graph=[]
for i in range(e):
    f,s,cost=map(int,input().split())
    graph.append([f,s,cost])#頂点0スタート

ans=0
for i in kruskal(v,graph):
    ans+=i[1]
print(ans)


