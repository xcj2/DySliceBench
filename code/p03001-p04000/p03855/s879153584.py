from collections import defaultdict
class UnionFind:


    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.n = n
    def find(self,x):
        if self.parent[x] == x:
            return x
        else:self.parent[x] = self.find(self.parent[x])
        x = self.parent[x]
        return x
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same(self,x,y):
        return bool(self.find(x)==self.find(y))

from sys import stdin
def main():
    N,K,L = map(int,stdin.readline().split())
    uf = UnionFind(N)
    uf1 = UnionFind(N)

    for _ in range(K):
        p,q = map(int,stdin.readline().split())
        uf.union(p-1,q-1)
    for _ in range(L):
        r,s = map(int,stdin.readline().split())
        uf1.union(r-1,s-1)
    d = defaultdict(int)
    for i in range(N):
        d[(uf.find(i),uf1.find(i))] += 1
    print(*(d[uf.find(i),uf1.find(i)]for i in range(N)))
    #print(l)

if __name__ == "__main__":
    main()