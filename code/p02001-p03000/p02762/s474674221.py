from collections import defaultdict
class UnionFind:
    def __init__(self, n=0):
        self.d = [-1 for _ in range(n)]
    
    def find(self, x): # find root
        if self.d[x] < 0: return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return False
        if -self.d[x] < -self.d[y]: # swap
            t = x
            x = y
            y = t
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.d[self.find(x)]
    

def main():
    N, M, K = map(int, input().split())
    uf = UnionFind(N)

    deg = [0 for _ in range(N)]
    for _ in range(M): # friends
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        deg[a] += 1
        deg[b] += 1
        uf.unite(a, b)
    # print(uf.d)

    to = [[] for _ in range(N)]
    for _ in range(K): # block
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        to[c].append(d)
        to[d].append(c)

    ret = []
    for i in range(N):
        ans = uf.size(i) - 1 - deg[i]
        for u in to[i]:
            if uf.same(i, u): ans -= 1
        ret.append(str(ans))

    print(' '.join(ret))


main()