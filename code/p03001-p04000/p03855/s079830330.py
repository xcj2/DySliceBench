from collections import Counter

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))

    def union(self, x, y):
        r = self.find(x)
        self.parents[r] = self.find(y)

    def find(self, x):
        path = [x]
        v = x
        while self.parents[v]!=v:
            v = self.parents[v]
            path.append(v)
        for p in path:
            self.parents[p] = v
        return v

if __name__=='__main__':
    n, k, l = map(int, input().split())

    road = UnionFind(n)
    for p, q in (map(int, input().split()) for _ in range(k)):
        road.union(p-1, q-1)

    railway = UnionFind(n)
    for r, s in (map(int, input().split()) for _ in range(l)):
        railway.union(r-1, s-1)

    groups = [str(road.find(i))+"&"+str(railway.find(i)) for i in range(n)]
    ctr = Counter(groups)

    print(*(ctr[g] for g in groups))