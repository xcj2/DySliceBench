import math
def P(n, r):
    return math.factorial(n)//math.factorial(n-r)
def C(n, r):
    return P(n, r)//math.factorial(r)


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ
        self.num = [1 for _ in range(n)]

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.num[y] += self.num[x]
            self.num[x] = 0
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
                
            self.num[x] += self.num[y]
            self.num[y] = 0

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def add(self, x, y):
        tmp = self.num[x]
        self.num[x] += self.num[y]
        self.num[y] += tmp
    
    
N, M = map(int, input().split()) 
L = [list(map(int, input().split())) for _ in range(M)]
L.reverse()


res = [C(N, 2)]
tmp = [0 for i in range(N)]
uf = UnionFind(N)

for i in range(M):
    L[i][0] -= 1
    L[i][1] -= 1
    if uf.same(L[i][0], L[i][1]) == False:
        res.append(res[-1] - uf.num[uf.find(L[i][0])] * uf.num[uf.find(L[i][1])])
        uf.unite(L[i][0], L[i][1])
    else:
        res.append(res[-1])
               
for i in range(1, M+1):
    print(res[-i - 1])