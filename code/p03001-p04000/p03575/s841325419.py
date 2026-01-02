import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]  # 親のノード番号
        self.rank = [0]*(n+1)
    def find(self,x):  # xの根のノード番号
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def same_check(self,x,y):  # x,yが同じグループか否か
        return self.find(x) == self.find(y)
    def unite(self,x,y):  # x,yの属するグループの併合
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            x,y = y,x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x


N,M = MI()
edges = [tuple(MI()) for _ in range(M)]

ans = 0
for i in range(M):
    U = UnionFind(N)
    for j in range(M):
        if j != i:
            a,b = edges[j]
            U.unite(a,b)
    x,y = edges[i]
    if not U.same_check(x,y):
        ans += 1

print(ans)
