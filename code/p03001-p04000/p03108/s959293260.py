N, M = map(int, input().split())
ab = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
 
 
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.rank = [0] * n
    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]
    def unite(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            if self.rank[pi] < self.rank[pj]:
                self.sizes[pj] += self.sizes[pi]
                self.parents[pi] = pj 
            else: 
                self.sizes[pi] += self.sizes[pj]
                self.parents[pj] = pi 
                if self.rank[pi] == self.rank[pj]:
                    self.rank[pi] += 1
        
def main():
    uf = UnionFind(N)
    p = N * (N - 1) // 2
    ans = [p]
    for x, y in reversed(ab):
        px = uf.find(x)
        py = uf.find(y)
        if px != py:
            p -= uf.sizes[px] * uf.sizes[py]
            uf.unite(px, py)
        ans.append(p)
 
    for a in reversed(ans[:-1]):
        print(a)
 
 
main()
