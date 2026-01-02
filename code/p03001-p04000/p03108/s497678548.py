class UnionFindTree:
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.__parents[self.find(x)]


def spline(func_=int, iter_=None):
    if iter_ is None:
        iter_ = input().split()
    return map(func_, iter_)


def main():
    n, m = spline()
    chains = UnionFindTree(n)
    f = lambda x: int(x) - 1
    bridges = [tuple(spline(func_=f)) for _ in range(m)]
    ans = [0] * m
    ans[-1] = n * (n - 1) // 2
    for i in range(m - 2, -1, -1):
        x, y = bridges.pop()
        tmp = ans[i + 1]
        if not chains.same(x, y):
            tmp -= chains.size(x) * chains.size(y)
            chains.union(x, y)
        ans[i] = tmp
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
