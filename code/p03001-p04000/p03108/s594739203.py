import array
import time

class UnionFind :
    def __init__(self, n):
        self.par = array.array('i', range(n))
        self.sizes = array.array('i', [1]*n)
        self.rank = array.array('i', [0]*n)


    def root(self, i):
        if i == self.par[i]:
            return i
        else:
            r = self.root(self.par[i])
            self.par[i] = r
            return r

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        srx = self.sized(x)
        sry = self.sized(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.par[rx] = ry
            else:
                self.par[ry] = rx
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] = self.rank[rx] + 1
            self.sizes[self.root(rx)] = srx + sry

    def same(self, x, y) :
        return self.root(x) == self.root(y)

    def sized(self, x):
        return self.sizes[self.root(x)]

    def debug(self):
        print(self.par)
        print(self.sizes)

def calsc(x):
    return (x * (x-1)) // 2

def main():
    (n,m) = map(int, input().split())
    ab = []
    for _ in range(m):
        (p,q) = map(int, input().split())
        ab.append((p-1,q-1))
    uf = UnionFind(n)
    res = []
    prev = 0
    while len(ab) > 0:
        (a,b) = ab.pop()
        #uf.debug()
        res.append(prev)
        score = prev
        if not uf.same(a,b):
            score = score - calsc(uf.sized(a)) - calsc(uf.sized(b))
            uf.unite(a,b)
            score = score + calsc(uf.sized(a))
        prev = score
    for i in range(len(res)):
        res[i] = calsc(n) - res[i]
    res = res[::-1]
    for r in res:
        print(r)

if __name__ == '__main__':
    main()
