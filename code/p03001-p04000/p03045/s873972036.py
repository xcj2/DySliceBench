import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def dfs(i,c):
    visited[i]=1
    col[i] = c
    for j in edge[i]:
        if not visited[j[0]]:
            if j[1]%2==0:
                dfs(j[0],c)
            else:
                dfs(j[0],-1*c)
class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0]*N
        self.count = 0
    def root(self, a):
        if self.parent[a]==a:
            return a
        else:
            self.parent[a]=self.root(self.parent[a])
            return self.parent[a]
    def size(x):
        return -par[root(x)]

    def is_same(self, a, b):
        return self.root(a)==self.root(b)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1

def main():
    dd = defaultdict(int)
    n,m=map(int, input().split())
    uf = UnionFind(n)

    for i in range(m):
        x,y,z=map(int, input().split())
        uf.unite(x-1,y-1)
    for i in range(n):
        dd[uf.root(i)]+=1
    print(len(dd))


if __name__ == '__main__':
    main()
