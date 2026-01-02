import collections
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
    n,m,k=map(int, input().split())
    friend = [0]*n
    fr = UnionFind(n)
    blocklist = [0]*n
    for i in range(m):
        a,b = map(int, input().split())
        fr.unite(a-1,b-1)
        friend[a-1]+=1
        friend[b-1]+=1
    for i in range(k):
        c,d=map(int, input().split())
        if(fr.root(c-1)==fr.root(d-1)):
            blocklist[c-1]+=1
            blocklist[d-1]+=1
    
    res = []
    dd = collections.defaultdict(int)
    for i in range(n):
        dd[fr.root(i)]+=1
    for i in range(n):
        res.append(dd[fr.root(i)]- blocklist[i] - friend[i]-1)
    print(*res)

if __name__ == '__main__':
    main()
