import sys
input = sys.stdin.readline

#########
class UnionFind():
    """
    parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
    find(x):要素xの属するグループの根を返す
    size(x):要素xの属するグループの要素数を返す
    same(x,y):x,yが同じグループに属しているか返す
    members(x):要素xが属するグループに属する要素をリストで返す
    roots(x):全ての根の要素を返す
    group_counte():グループの数を返す
    all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
    """
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    
def Kruskal(V,edges):
        """
        V:node数
        edges:[u,v,cost]の辺のリスト
        
        return: 最小全域木のコストの和
        """
        #edges = sorted(edges, key=lambda x: x[2])  # costでself.edgesをソートする
        res = 0
        uf=UnionFind(V)
        for e in edges:
            if not uf.same(e[0], e[1]):
                uf.union(e[0], e[1])
                res += e[2]
        return res

############

N,M=map(int,input().split())
edges=[]

for i in range(M):
    x,y,z=map(int,input().split())
    edges.append((x-1,y-1,1))
    
E=Kruskal(N,edges)
print(N-E)




