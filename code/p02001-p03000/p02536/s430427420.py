import sys

sys.setrecursionlimit(10**7)
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
UF = UnionFind(N)
for _ in range(M):
    a,b = MI()
    UF.unite(a,b)

A = UF.par
A = [UF.find(A[i]) for i in range(1,N+1)]

print(len(set(A))-1)
