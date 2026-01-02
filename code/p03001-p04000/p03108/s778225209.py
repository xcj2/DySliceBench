import sys
sys.setrecursionlimit(10 ** 6)


class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, a):
        p = self.parent[a]
        if p == a:
            return a
        q = self.root(p)
        self.parent[a] = q
        return q

    def merge(self, a, b):
        '''merge a into b'''
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return False
        self.parent[a] = b
        self.size[b] = self.size[a] + self.size[b]
        return True

    def get_size(self, a):
        a = self.root(a)
        return self.size[a]


def main():
    n, m = map(int, input().split())
    tree = [[int(a)-1 for a in input().split()] for _ in range(m)]
    uf = UnionFind(n)
    sep = []
    sep_prev = n * (n - 1) // 2
    for a, b in tree[::-1]:
        asize = uf.get_size(a)
        bsize = uf.get_size(b)
        sep.append(sep_prev)
        success = uf.merge(a, b)
        if success:
            sep_prev -= asize * bsize

    for s in sep[::-1]:
        print(s)


main()
