class UnionFind:
    MAX_N = 0
    PAR  = [] 
    RANK = []

    def __init__(self,n):
        self.MAX_N = n
        self.PAR = [ i for i in range(n)]
        self.RANK= [ 0 ] * n

    def find(self,x):
        if self.PAR[x] == x:
            return x
        else:
            self.PAR[x] = self.find(self.PAR[x])
            return self.PAR[x] 

    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.RANK[x] < self.RANK[y]:
            self.PAR[x] = y
        else:
            self.PAR[y] = x
            if self.RANK[x] == self.RANK[y]:
                self.RANK[x] += 1

    def same(self,x,y):
        return self.find(x) == self.find(y)

def kruskal(Edge):
    Edge.sort(key=lambda x:x[2])
    data = UnionFind(V)
    res = 0
    for i in range(E):
        u = Edge[i][0]
        v = Edge[i][1]
        d = Edge[i][2]
        if data.same(u,v) == False:
            data.unite(u,v)
            res += d
    return res

V,E = map(int,input().split())
Edge = []
for _ in range(E):
    Edge.append(list(map(int,input().split())))

ans = kruskal(Edge)
print(ans)

