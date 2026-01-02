class UnionFindTree:
    __slots__ = ('__parents', )

    def __init__(self, n):
        self.__parents = [-1] * n

    def find(self, x):
        p = self.__parents
        if p[x] < 0:
            return x
        parent = self.find(p[x])
        p[x] = parent
        return parent

    def union(self, x, y):
        p = self.__parents
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if p[x] > p[y]:
            x, y = y, x
        p[x] += p[y]
        p[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.__parents[self.find(x)]


def spline(func_=int, iter_=None):
    if iter_ is None:
        iter_ = input().split()
    return map(func_, iter_)


def main():
    n, m, k = spline()
    similar = UnionFindTree(n)
    candidates = [-1] * n
    for _ in range(m):
        a, b = spline()
        a -= 1
        b -= 1
        similar.union(a, b)
        candidates[a] -= 1
        candidates[b] -= 1
    for i in range(n):
        candidates[i] += similar.size(i)
    for _ in range(k):
        c, d = spline()
        c -= 1
        d -= 1
        if similar.same(c, d):
            candidates[c] -= 1
            candidates[d] -= 1
    print(*candidates, sep=' ')


if __name__ == "__main__":
    main()
