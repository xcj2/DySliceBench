class UnionFind:
    def __init__(self, N):
        self.parent = [x for x in range(N+1)]
        self.rank = [1 for x in range(N+1)]

    def find(self, x):
        p = x
        while self.parent[p] != p:
            p = self.parent[p]
        self.parent[x] = p
        return p

    def union(self, r, l):
        x, y = self.find(r), self.find(l)
        if x == y:
            return
        rx, ry = self.rank[x], self.rank[y]
        if rx > ry:
            self.parent[y] = x
        elif rx == ry:
            self.parent[y] = x
            self.rank[x] += 1
        else:
            self.parent[x] = y

def main():
    N, K, L = map(int, input().split())
    
    rails = UnionFind(N)
    for _ in range(K):
        p, q = map(int, input().split())
        rails.union(p, q)

    loads = UnionFind(N)
    for _ in range(L):
        p, q = map(int, input().split())
        loads.union(p,q)
    RL = [(rails.find(u), loads.find(u)) for u in range(1, N+1)]
    from collections import Counter
    c = Counter(RL)

    print(*(c[x] for x in RL))

main()

