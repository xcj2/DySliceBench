# 64 Kruskal


class UnionFind():
    def __init__(self, v):
        self.rank = [1] * v
        self.par = [x for x in range(v)]
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        if self.find(x) == self.find(y):
            return False
        else:
            p_x = self.find(x)
            p_y = self.find(y)
            if self.rank[p_x] >= self.rank[p_y]:
                self.par[p_y] = p_x
                self.rank[p_y] += 1
            else:
                self.par[p_x] = p_y
                self.rank[p_x] += 1
    
    def same(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        return p_x == p_y
    
v, e = map(int, input().split())
e_l = [[int(x) for x in input().split()] for y in range(e)]
e_l.sort(key= lambda x: x[2])

def Kruskal(s):
    ans = 0
    uf = UnionFind(v)

    for _s, _t, _w in e_l:
        if not uf.same(_s, _t):
            uf.unite(_s, _t)
            ans += _w
    return ans
            
print(Kruskal(0))
