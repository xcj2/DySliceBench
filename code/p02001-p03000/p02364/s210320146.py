class UnionFindTree():

    def __init__(self, n):
        #木全体の要素数
        self.n  = n
        #root[x]<0ならそのノードが根でありその値が木の要素数
        self.root = [-1] * (n+1)
        #ランク
        self.rank = [1] * (n+1)

    def find_root(self,x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self,x,y):
        return self.find_root(x) == self.find_root(y)

    def count_node(self,x):
        return -1 * self.root[self.find_root(x)]
v, e = map(int, input().split())
edges = []
for _ in range(e):
    s, t, w = map(int, input().split())
    edges.append((w, s, t))

#edgesは予めsortする
edges.sort()

def kuruskal(n, edges):
    uft = UnionFindTree(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not uft.is_same(s, t):
            res += w
            uft.unite(s, t)
    return res

print(kuruskal(v, edges))
