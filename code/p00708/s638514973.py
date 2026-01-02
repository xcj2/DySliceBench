class DisjointSets:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.siz = [1]*n

    def root(self,x):
        if x != self.parent[x]: 
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self,x,y): 
        return self.root(x) == self.root(y)

    def unite(self,x,y): 
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.siz[x] < self.siz[y]:
            x,y = y,x
        self.parent[y] = x
        self.siz[x] += self.siz[y]

    def size(self,x):
        return self.siz[self.root(x)]

def length(a,b):
    x1,y1,z1,r1 = cell[a]
    x2,y2,z2,r2 = cell[b]
    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5-r1-r2

while True:
    n = int(input())
    if not n: break
    cell = [[float(i) for i in input().split()] for _ in range(n)]
    corri = []
    ds = DisjointSets(n)
    for i in range(n):
        for j in range(i+1,n):
            l = length(i,j)
            if l <= 0: ds.unite(i,j)
            else: corri.append((l,i,j))
    corri.sort(key = lambda x:x[0])
    sumlen = 0
    for l,a,b in corri:
        if ds.same(a,b): continue
        sumlen += l
        ds.unite(a,b)
    print(f"{sumlen:.3f}")
