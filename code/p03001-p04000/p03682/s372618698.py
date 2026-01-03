n=int(input())
l=[]
for i in range(n):
    l.append([i]+list(map(int,input().split())))
g = []
l.sort(key=lambda x: x[1])
for i in range(n-1):
    g.append([l[i][0],l[i+1][0],abs(l[i][1]-l[i+1][1])])
l.sort(key=lambda x: x[2])
for i in range(n-1):
    g.append([l[i][0],l[i+1][0],abs(l[i][2]-l[i+1][2])])

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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def minimum_spanning_tree(g,n):
#g=list、「始点、終点、辺の重み」
#n=頂点数
    g.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    ret = 0
    for sg in g:
        a,b,c = sg[0],sg[1],sg[2]
        if not uf.same(a,b):
            uf.union(a,b)
            ret += c
    return ret

print(minimum_spanning_tree(g,n))