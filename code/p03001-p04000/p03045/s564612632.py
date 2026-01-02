import sys


sys.setrecursionlimit(10**5)


class UnionFind(object):
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def merge(self, a, b):
        pa = self.root(a)
        pb = self.root(b)
        self.parent[pa] = pb
    
    def root(self, x):
        p = self.parent[x]
        if p == x:
            return x
        else:
            r = self.root(p)
            self.parent[x] = r
            return r


def main():
    N, M = map(int, input().split())

    uf = UnionFind(N)
    for _ in range(M):
        x, y, _ = map(int, input().split())
        uf.merge(x-1, y-1)

    print(len(list(filter(lambda x: x == uf.root(x), range(N)))))


main()