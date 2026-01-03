n = int(input())
xy = []
for i in range(n):
    tmp = list(map(int,input().split()))
    tmp.append(i)
    xy.append(tmp)
link = []

xy.sort(key=lambda x:x[0])
for i in range(n-1):
    x1,_,node1 = xy[i]
    x2,_,node2 = xy[i+1]
    cost = abs(x1-x2)
    link.append([node1,node2,cost])

xy.sort(key=lambda x:x[1])
for i in range(n-1):
    _,y1,node1 = xy[i]
    _,y2,node2 = xy[i+1]
    cost = abs(y1-y2)
    link.append([node1,node2,cost])
class UnionFind():
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

def krs(g,num_v):
    g.sort(key=lambda x:x[2])

    uf = UnionFind(num_v)
    mst = []
    for edge in g:
        if not uf.same(edge[0], edge[1]):
            uf.union(edge[0], edge[1])
            mst.append(edge)
    return mst


ret = krs(link,n)
ans=0
for i in range(len(ret)):
    ans+=ret[i][2]
print(ans)
